from django.shortcuts import render
from .models import services

# Create your views here.
def home(request):
    service = services.objects.all()
    



    return render(request,'index.html',{'service':service});

def terms(request):
    return render(request,'terms-conditions.html')