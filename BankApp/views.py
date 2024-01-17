from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from .models import SendMoney,LoanRequest
from .serializers import SendMoneySerializer,SendMoneyListSerializer,MySendMoneyListSerializer,LoanRequestSerializer,LoanRequestListSerializer,LoanRequestDetailSerializer,UserLoanRequestDetailSerializer,UserLoanRequestUpdateSerializer,AcceptedLoanSerializer,AcceptedLoanDetailSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsManager
# Create your views here.

# Sending Money
class SendMoneyView(CreateAPIView):
    queryset = SendMoney.objects.all()
    serializer_class = SendMoneySerializer
    permission_classes = [IsAuthenticated]

class SendMoneyListView(ListAPIView):
    queryset = SendMoney.objects.all()
    serializer_class = SendMoneyListSerializer
    permission_classes = [IsManager]
 
class MySendMoneyListView(ListAPIView):
    # queryset = SendMoney.objects.all()
    serializer_class = MySendMoneyListSerializer
    permission_classes = [IsAuthenticated]
 
    def get_queryset(self):
        return SendMoney.objects.filter(sender=self.request.user) | SendMoney.objects.filter(receiver=self.request.user)

# Loans
class LoanRequestView(CreateAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoanRequestListView(ListAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestListSerializer
    permission_classes = [IsManager]

class LoanRequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = LoanRequestDetailSerializer
    permission_classes = [IsManager]

class UserLoanRequestDetailView(ListAPIView):
    # queryset = LoanRequest.objects.all()
    serializer_class = UserLoanRequestDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanRequest.objects.filter(user=self.request.user)

class UserLoanRequestUpdateView(RetrieveUpdateDestroyAPIView):
    # queryset = LoanRequest.objects.all()
    serializer_class = UserLoanRequestUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanRequest.objects.filter(user=self.request.user)
    
class AcceptedLoanListView(ListAPIView):
    serializer_class =  AcceptedLoanSerializer
    permission_classes = [IsManager]
    
    def get_queryset(self):
        # Filter loan requests where is_approved is True
        return LoanRequest.objects.filter(is_approved=True)

class AcceptedLoanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = LoanRequest.objects.all()
    serializer_class = AcceptedLoanDetailSerializer
    permission_classes = [IsManager]