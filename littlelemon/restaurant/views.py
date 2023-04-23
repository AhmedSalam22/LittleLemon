from django.shortcuts import render
# from .serializers import MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer, BookingSerializer
from .models import Booking, Menu
from rest_framework.viewsets import ModelViewSet

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    



    