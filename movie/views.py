from django.shortcuts import render, redirect
from .models import Review  

# Create your views here.

def index(request):
    return redirect('movie:index')