from django.shortcuts import render
from .models import dest
# Create your views here.

def index(request):
    dess=dest.objects.all()
    return render(request,'index.html',{'dess':dess})