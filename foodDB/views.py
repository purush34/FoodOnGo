from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .serializers import foodSerializer

# Create your views here.

from .models import HotelMenu


def index(request):
    context={
    'iterator':range(1,10),
    'all_hotelMenu':HotelMenu.objects.filter(),
    }
    allh = HotelMenu.objects.filter()
    print(allh)
    for i in allh.values():
        print(i)
    return render(request,'index.html',context)

def getHotelMenu(request,hotelName):
    if hotelName == "Andhra":
        hotelName = "Andhra Ruchulu"
    elif hotelName == "Lovesugar":
        hotelName = "Love sugar"
    elif hotelName == "Amritam":
        hotelName = "Amritam"
    elif hotelName == "Chetashop":
        hotelName = "Cheta shop"
    elif hotelName == "CasaBlanka":
        hotelName = "Casa blanka"
    elif hotelName == "Spicy villa":
        hotelName = "Spicy villa"
    else:
        hotelName = "Andhra Ruchulu"
    context={
    'iterator':range(1,10),
    'all_hotelMenu':HotelMenu.objects.filter(HotelName=hotelName),
    }
    print()
    print()
    print()
    allh = HotelMenu.objects.filter(HotelName=hotelName)
    print(allh)
    return render(request,'index.html',context)