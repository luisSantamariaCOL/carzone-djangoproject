from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'This is error message')
        return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('pages:home')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
