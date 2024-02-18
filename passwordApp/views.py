from django.shortcuts import render
from .models import Password

def index(request):
    passwords = Password.objects.order_by('-name')
    return render(request, "passwordApp/index.html", {'passwords': passwords})
