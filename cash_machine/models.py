from django.db import models

from atm.models import AbstractModel


class CardAccount(AbstractModel):
    class Meta(AbstractModel.Meta):
        db_table = 'card_account'

    card_number = models.CharField(max_length=16, unique=True, blank=False, null=False, db_index=True)
    balance = models.IntegerField()
    # TODO encrypt pin
    pin = models.IntegerField(null=False, blank=False)
    wrong_pin_counter = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.card_number}'


class Transaction(AbstractModel):
    class Meta(AbstractModel.Meta):
        db_table = 'transaction'

    BALANCE = 1
    WITHDRAW = 2

    OPERATION_CODE_CHOICES = [
        (BALANCE, 'Balance'),
        (WITHDRAW, 'Withdraw'),
    ]

    card = models.ForeignKey(CardAccount, null=False, blank=False, on_delete=models.PROTECT)
    operation_code = models.PositiveSmallIntegerField(null=False, blank=False, choices=OPERATION_CODE_CHOICES)
    withdraw_amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.card.card_number} -- {self.operation_code} -- {self.withdraw_amount}'
