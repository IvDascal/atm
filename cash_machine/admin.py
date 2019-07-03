from django.contrib import admin

from cash_machine.models import CardAccount, Transaction

admin.site.register(CardAccount)
admin.site.register(Transaction)
