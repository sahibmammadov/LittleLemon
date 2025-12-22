from django.shortcuts import render
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request, 'indexs.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

