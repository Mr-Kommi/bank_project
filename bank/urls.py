from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw),
    path('transfer/', views.transfer),
    path('statement/', views.statement),
    path('accounts/', views.accounts),
    path('transactions/', views.transactions),
    path('transactions/<int:account_id>/', views.transactions_for_account),
]
