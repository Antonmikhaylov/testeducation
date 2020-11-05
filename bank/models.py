from django.db import models


class Bank(models.Model):

    BANK = 'bank'
    MFO = 'mfi'

    BANK_TYPE = (
        (BANK, 'Банк'),
        (MFO, 'Мфо')
    )

    bank_type = models.CharField(
        max_length=5,
        verbose_name='Тип банка',
        choices=BANK_TYPE,
        default=MFO,
        db_index=True,
    )
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return self.name
