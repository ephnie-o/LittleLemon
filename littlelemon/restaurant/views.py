from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuTable, BookingTable
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import MenuTableSerializer, BookingTableSerializer, UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuTableSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]