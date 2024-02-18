from django.shortcuts import render, redirect
from .models import Password
from .forms import PasswordForm

def index(request):
    passwords = Password.objects.order_by('-name')
    return render(request, "passwordApp/index.html", {'passwords': passwords})

def create(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordForm()

    return render(request, 'passwordApp/create.html', {'form': form})

def edit(request, password_id):
    password = Password.objects.get(pk=password_id)
    if request.method == 'POST':
        form = PasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordForm(instance=password) 

    return render(request, 'passwordApp/edit.html', {'form': form})

def delete(request, password_id):
    password = Password.objects.get(pk=password_id)
    password.delete()
    return redirect('index')