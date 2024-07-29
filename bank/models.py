from django.db import models

class Account(models.Model):
    iban = models.CharField(max_length=34, unique=True)
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.iban

class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    balance = models.FloatField()

    def __str__(self):
        return f"{self.account.iban} - {self.amount} on {self.date}"
