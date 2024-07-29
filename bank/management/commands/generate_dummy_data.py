import faker
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from bank.models import Account, Transaction
from django.utils import timezone

class Command(BaseCommand):
    help = 'Generate dummy data for accounts and transactions'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()

        # Create some accounts
        accounts = []
        for i in range(10):
            iban = f"DE89370400404432013{i:02d}"
            balance = fake.random_int(min=100, max=1000)
            account = Account.objects.create(iban=iban, balance=balance)
            accounts.append(account)

        # Create some transactions
        for account in accounts:
            for _ in range(10):
                date = fake.date_time_between(start_date=timezone.now() - timedelta(days=30), end_date=timezone.now())
                amount = fake.random_int(min=-100, max=100)
                balance = account.balance + amount
                transaction = Transaction.objects.create(account=account, date=date, amount=amount, balance=balance)
                account.balance = balance
                account.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))
