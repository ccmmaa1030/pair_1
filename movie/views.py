from django.shortcuts import render, redirect
from .models import Review  

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    
    context = {
        "reviews": reviews,
    }
    return render(request, 'movie/index.html', context)

def new(request):
    return render(request, 'movie/new.html')