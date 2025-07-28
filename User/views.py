from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def user_register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration Successful. You can now log in!")
            login(request, user)
            return redirect('index')
            messages.error(request, message='Registration Unsuccessful. Invalid information. Please try again.')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = MyUserLoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get('email')
            user_password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_email, password=user_password)

            if user:
                login(request, user)
                messages.success(request, "You successfully logged in! Welcome, " + user.username + " !")
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Fill the form correctly.")
    else:
        form = MyUserLoginForm()

    return render(request, 'login.html', {'form': form})

def user_logout_view(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect('index')