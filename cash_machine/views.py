import datetime

from django.shortcuts import render, redirect

from cash_machine.models import CardAccount, Transaction


def index(request):
    """
    View for start page: card number processing.

    If card number exists and card is not blocked go to pin enter page.
    Otherwise display error page.

    Store card id into session.
    """

    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card_number = card_number.replace('-', '')

        try:
            card = CardAccount.objects.get(card_number=card_number)
        except:
            card = None

        if not card:
            request.session['error'] = {'error_msg': 'Неверный номер карты', 'error_back': '/'}
            return redirect('error')

        if card.is_blocked:
            request.session['error'] = {'error_msg': 'Ваша карта заблокирована', 'error_back': '/'}
            return redirect('error')
        else:
            request.session['card_id'] = card.pk
            return redirect('pin')
    else:
        return render(request, 'cash_machine/index.tpl')


def pin(request):
    """
    View for pin processing.


    If pin entered by user matches to card pin go to transaction page.
    Otherwise display error page.

    User has 4 attempts to enter pin.
    After the 4th wrong attempt, the map is blocked and the error page is displayed.
    """

    if request.method == 'POST':
        card_pin = request.POST.get('pin')
        card_id = request.session.get('card_id')

        card = CardAccount.objects.get(pk=card_id)

        if card_pin and int(card_pin) == card.pin:
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

            request.session['error_msg'] = {'error_msg': 'Ваша карта заблокирована', 'error_back': '/'}

            return redirect('error')

    return render(request, 'cash_machine/pin.tpl')


def transaction(request):
    """
    View for transaction.

    User has 2 options:
    1) show card balance
    2) withdraw cash
    """
    return render(request, 'cash_machine/transaction.tpl')


def balance(request):
    """
    View to show card balance.

    This operation is registered in transaction table.
    """
    card_id = request.session.get('card_id')
    card = CardAccount.objects.get(pk=card_id)
    today = datetime.date.today()
    operation = Transaction()
    operation.card = card
    operation.operation_code = Transaction.BALANCE
    operation.save()

    return render(request, 'cash_machine/balance.tpl', {'card': card, 'today': today})


def withdraw(request):
    """
    View for withdraw processing.


    If the withdrawn amount is less than or equal to the balance on the card,
    the balance on the card is reduced by this amount.

    This operation is registered in transaction table and go to transaction report page.

    Otherwise display error page.
    """
    if request.method == 'POST':
        amount = request.POST.get('amount')

        if not amount:
            request.session['error'] = {'error_msg': 'Необходимо ввести сумму', 'error_back': 'withdraw'}

            return redirect('error')

        amount = int(amount)
        card_id = request.session.get('card_id')
        card = CardAccount.objects.get(pk=card_id)

        if amount <= card.balance:
            operation = Transaction()
            operation.card = card
            operation.operation_code = Transaction.WITHDRAW
            operation.withdraw_amount = amount
            operation.save()

            card.balance -= amount
            card.save()

            request.session['transaction_id'] = operation.pk

            return redirect('report')

        else:
            request.session['error'] = {'error_msg': 'Недостаточно денежных средств на карте', 'error_back': 'withdraw'}

            return redirect('error')

    return render(request, 'cash_machine/withdraw.tpl')


def error(request):
    """
    View to display error page.
    """
    error_dict = request.session.get('error')
    return render(request, 'cash_machine/error.tpl', {'error': error_dict})


def report(request):
    """
    View to display transaction report.
    """
    transaction_id = request.session.get('transaction_id')
    operation = Transaction.objects.get(pk=transaction_id)

    return render(request, 'cash_machine/report.tpl', {'transaction': operation})
