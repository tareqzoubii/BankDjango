from django.urls import path
from .views import CustomerCreateView,CustomerListView,CustomerRetrieveUpdateView

urlpatterns = [
    path('createCustomer/', CustomerCreateView.as_view()), # for regestration
    path('customers/',CustomerListView.as_view()),
    path('me/',CustomerRetrieveUpdateView.as_view()),
]