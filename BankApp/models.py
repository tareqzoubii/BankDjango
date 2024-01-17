from django.db import models
from accounts.models import CustomUser
# Create your models here.

class SendMoney(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_transactions', on_delete=models.CASCADE)
    the_amount = models.PositiveIntegerField()  # Ensure the amount is non-negative

LOAN_TYPES = (
    ('Real Estate', 'Real Estate'),
    ('Transport', 'Transport'),
)

class LoanRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.PositiveIntegerField()
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    is_approved = models.BooleanField(default=False)