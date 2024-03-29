from django.urls import path
from . import views
from .views import create

urlpatterns = [
    path('', views.index, name='index'),
    path('create.html/', create, name='create'),
    path('edit/<int:password_id>/', views.edit, name='edit'),
    path('delete/<int:password_id>/', views.delete, name='delete'),
    path('export/', views.export_passwords_csv, name='export_passwords_csv'),
    path('import/', views.import_passwords_csv, name='import_passwords_csv'),
]