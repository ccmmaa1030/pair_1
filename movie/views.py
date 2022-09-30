from django.shortcuts import render, redirect
from .models import Review  

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    
    context = {
        "reviews": reviews,
    }
    return render(request, 'movie/index.html', context)

def detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        "review": review,
    }
    return render(request, 'movie/detail.html', context)

def new(request):
    return render(request, 'movie/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Review.objects.create(content=content, title=title)
    return redirect('movie:index')

def delete(request, pk):
    Review.objects.get(id=pk).delete()
    return redirect('movie:index')

def edit(request, pk):
    review = Review.objects.get(id=pk)

    context = {
        "review": review,
    }
    return render(request, 'movie/edit.html', context)

def update(request, pk):
    review = Review.objects.get(id=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')

    review.title = title
    review.content = content

    review.save()

    return redirect("movie:index")
