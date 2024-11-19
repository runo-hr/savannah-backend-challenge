from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Orders System")


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
