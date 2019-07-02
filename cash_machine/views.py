from django.shortcuts import render


def index(request):

    return render(request, 'cash_machine/index.tpl')

