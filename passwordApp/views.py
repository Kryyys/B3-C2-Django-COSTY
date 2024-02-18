from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Password
from .forms import PasswordForm
import csv

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

def export_passwords_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'URL', 'Pseudonym', 'Password'])

    passwords = Password.objects.all()
    for password in passwords:
        writer.writerow([password.name, password.url, password.pseudonym, password.password])

    return response

def import_passwords_csv(request):
    if request.method == 'POST' and 'csv_file' in request.FILES:
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            password = Password.objects.create(
                name=row['Name'],
                url=row['URL'],
                pseudonym=row['Pseudonym'],
                password=row['Password']
            )
            password.save()

        return redirect('index')

    return render(request, 'passwordApp/import.html')