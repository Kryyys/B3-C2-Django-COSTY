from django.urls import path
from . import views
from .views import create

urlpatterns = [
    path('', views.index, name='index'),
    path('create.html/', create, name='create'),
    path('edit/<int:password_id>/', views.edit, name='edit')
]