from django.shortcuts import render, redirect

from cash_machine.models import CardAccount


def index(request):
    context = {
        'input_type': 'card_number'
    }

    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        card = CardAccount.objects.get(card_number=card_number)
        request.session['card_id'] = card.pk

        return redirect('pin')
    else:
        return render(request, 'cash_machine/index.tpl', context)


def pin(request):
    context = {
        'input_type': 'pin'
    }

    if request.method == 'POST':
        card_pin = request.POST.get('pin')
        card_id = request.session.get('card_id')

        card = CardAccount.objects.get(pk=card_id)

        if int(card_pin) == card.pin:
            return redirect('transaction')
            # else redirect to error page

    return render(request, 'cash_machine/pin.tpl', context)


def transaction(request):
    return render(request, 'cash_machine/transaction.tpl')
