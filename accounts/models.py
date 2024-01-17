import random
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('Customer', 'Customer'),
    ('Manager', 'Manager'),
)

def generate_account_number():
    return random.randint(10**11, 10**12 - 1)

class CustomUser(AbstractUser):
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    account_amount = models.IntegerField(default=0.00)
    role = models.CharField(max_length=8, choices=ROLES, default='Customer')
    account_number = models.BigIntegerField(default = generate_account_number, primary_key=True)

    # Add or change related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
