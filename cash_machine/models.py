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
