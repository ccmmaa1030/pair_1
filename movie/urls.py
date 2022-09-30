from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    # path('detail/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    # path('edit/', views.edit, name='edit'),
]