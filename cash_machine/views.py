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
    card_id = request.session.get('card_id')
    print(card_id)
    return render(request, 'cash_machine/pin.tpl', context)
