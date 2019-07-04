import datetime

from django.shortcuts import render, redirect

from cash_machine.models import CardAccount, Transaction


def index(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card_number = card_number.replace('-', '')

        try:
            card = CardAccount.objects.get(card_number=card_number)
        except:
            card = None

        if not card:
            request.session['error_msg'] = 'Card does not exist'
            return redirect('error')

        if card.is_blocked:
            request.session['error_msg'] = 'Your card is blocked'
            return redirect('error')
        else:
            request.session['card_id'] = card.pk
            return redirect('pin')
    else:
        return render(request, 'cash_machine/index.tpl')


def pin(request):
    if request.method == 'POST':
        card_pin = request.POST.get('pin')
        card_id = request.session.get('card_id')

        card = CardAccount.objects.get(pk=card_id)

        if int(card_pin) == card.pin:
            return redirect('transaction')

        elif card.wrong_pin_counter < 3:
            card.wrong_pin_counter += 1
            card.save()

            remaining_attempts = 4 - card.wrong_pin_counter
            error_msg = 'Неправильный PIN. Осталось попыток: {} '.format(remaining_attempts)

            return render(request, 'cash_machine/pin.tpl', {'error_msg': error_msg})

        else:
            card.is_blocked = True
            card.save()

            request.session['error_msg'] = 'Your card is blocked because of wrong pin'

            return redirect('error')

    return render(request, 'cash_machine/pin.tpl')


def transaction(request):
    return render(request, 'cash_machine/transaction.tpl')


def balance(request):
    card_id = request.session.get('card_id')
    card = CardAccount.objects.get(pk=card_id)
    today = datetime.date.today()
    operation = Transaction()
    operation.card = card
    operation.operation_code = Transaction.BALANCE
    operation.save()

    return render(request, 'cash_machine/balance.tpl', {'card': card, 'today': today})


def withdraw(request):
    return render(request, 'cash_machine/withdraw.tpl')


def error(request):
    error_msg = request.session.get('error_msg')
    return render(request, 'cash_machine/error.tpl', {'error_message': error_msg})
