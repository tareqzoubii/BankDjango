from rest_framework import serializers
from .models import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'id_number', 'phone_number', 'account_amount', 'role')

class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('account_number','username','first_name','last_name','email','id_number','phone_number','account_amount','role')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('account_number','username','first_name','last_name','email','id_number','phone_number','account_amount')