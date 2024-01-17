from rest_framework import serializers
from .models import SendMoney,LoanRequest
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework import status

class SendMoneySerializer(serializers.Serializer):
    receiver_account_number = serializers.IntegerField()
    the_amount = serializers.IntegerField()

    def create(self, validated_data):
        sender = self.context['request'].user
        receiver_account_number = validated_data['receiver_account_number']
        the_amount = validated_data['the_amount']

        try:
            receiver = CustomUser.objects.get(account_number=receiver_account_number)
        except CustomUser.DoesNotExist:
            return {'message': 'Receiver not found'}, status.HTTP_404_NOT_FOUND

        if sender.account_amount >= the_amount > 0:
            sender.account_amount -= the_amount
            sender.save()
            receiver.account_amount += the_amount
            receiver.save()

            SendMoney.objects.create(sender=sender, receiver=receiver, the_amount=the_amount)

            return Response({'message': 'Money sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Insufficient balance or invalid amount'}, status=status.HTTP_400_BAD_REQUEST)
        
class SendMoneyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMoney
        fields = '__all__'
 
class MySendMoneyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMoney
        fields = '__all__'

# Loans
class LoanRequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = LoanRequest
        fields = ['user','amount','period','loan_type']

class LoanRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'

class LoanRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'

class UserLoanRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = '__all__'

class UserLoanRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['amount','period','loan_type']

class AcceptedLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['id','user','amount','period','loan_type','is_approved']

class AcceptedLoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequest
        fields = ['user','is_approved']