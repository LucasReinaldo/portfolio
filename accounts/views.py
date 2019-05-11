from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def signin(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password'] == request.POST['password1']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/signin.html', {'error': 'Email has already been in use.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signin.html', {'error': 'Passwords must match.'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signin.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Email or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
