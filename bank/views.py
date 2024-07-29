from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

@api_view(['POST'])
def deposit(request):
    data = request.data
    try:
        account = Account.objects.get(iban=data['iban'])
        account.balance += data['amount']
        account.save()
        transaction = Transaction(account=account, amount=data['amount'], balance=account.balance)
        transaction.save()
        return Response({"message": "Deposit successful"}, status=status.HTTP_200_OK)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def withdraw(request):
    data = request.data
    try:
        account = Account.objects.get(iban=data['iban'])
        if account.balance >= data['amount']:
            account.balance -= data['amount']
            account.save()
            transaction = Transaction(account=account, amount=-data['amount'], balance=account.balance)
            transaction.save()
            return Response({"message": "Withdrawal successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def transfer(request):
    data = request.data
    try:
        from_account = Account.objects.get(iban=data['from_iban'])
        to_account = Account.objects.get(iban=data['to_iban'])
        if from_account.balance >= data['amount']:
            from_account.balance -= data['amount']
            from_account.save()
            to_account.balance += data['amount']
            to_account.save()
            Transaction(account=from_account, amount=-data['amount'], balance=from_account.balance).save()
            Transaction(account=to_account, amount=data['amount'], balance=to_account.balance).save()
            return Response({"message": "Transfer successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
    except Account.DoesNotExist:
        return Response({"error": "One or both accounts not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def statement(request):
    iban = request.query_params.get('iban')
    sort_order = request.query_params.get('sort', 'desc')
    page = int(request.query_params.get('page', 1))
    per_page = 10

    try:
        account = Account.objects.get(iban=iban)
        if sort_order == 'asc':
            transactions = Transaction.objects.filter(account=account).order_by('date')
        elif sort_order == 'desc':
            transactions = Transaction.objects.filter(account=account).order_by('-date')
        else:
            return Response({"error": "Invalid sort order. Use 'asc' or 'desc'."}, status=status.HTTP_400_BAD_REQUEST)

        total = transactions.count()
        transactions = transactions[(page-1)*per_page:page*per_page]

        statement = TransactionSerializer(transactions, many=True).data
        return Response({
            "statement": statement,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "pages": (total // per_page) + (1 if total % per_page else 0),
                "next": page + 1 if (page * per_page < total) else None,
                "prev": page - 1 if page > 1 else None,
                "first": 1,
                "last": (total // per_page) + (1 if total % per_page else 0)
            }
        })
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def accounts(request):
    accounts = Account.objects.all()
    return Response(AccountSerializer(accounts, many=True).data)

@api_view(['GET'])
def transactions(request):
    transactions = Transaction.objects.all()
    return Response(TransactionSerializer(transactions, many=True).data)

@api_view(['GET'])
def transactions_for_account(request, account_id):
    transactions = Transaction.objects.filter(account_id=account_id)
    return Response(TransactionSerializer(transactions, many=True).data)
