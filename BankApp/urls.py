from django.urls import path
from .views import SendMoneyView,SendMoneyListView,MySendMoneyListView,LoanRequestView,LoanRequestListView,LoanRequestDetailView,UserLoanRequestDetailView,UserLoanRequestUpdateView,AcceptedLoanListView,AcceptedLoanDetailView

urlpatterns = [
    path('send-money/', SendMoneyView.as_view()),
    path('transactions/', SendMoneyListView.as_view()),
    path('my-transactions/', MySendMoneyListView.as_view()),
    path('request-loan/', LoanRequestView.as_view()),
    path('loan-requests/', LoanRequestListView.as_view()),
    path('loan-requests/<pk>/', LoanRequestDetailView.as_view()),
    path('my-requests/', UserLoanRequestDetailView.as_view()),
    path('my-requests/<pk>/', UserLoanRequestUpdateView.as_view()),
    path('accepted-loans/', AcceptedLoanListView.as_view()),
    path('accepted-loans/<pk>/', AcceptedLoanDetailView.as_view()),
]