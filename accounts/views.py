from django.shortcuts import render
from .models import CustomUser
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateAPIView
from .serializers import CreateUserSerializer,ListUsersSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsManager,IsOwnerOrReadOnly,IsNotAuthenticated
# Create your views here.

class CustomerCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        # Create the user without saving to the database
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Set the user's password
        password = request.data.get('password')
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomerListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListUsersSerializer
    permission_classes = [IsManager]

class CustomerRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user