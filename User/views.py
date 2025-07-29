from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .services import *
from django.conf import settings
from .models import MyUser as User


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
                otp_code = generate_OTP_code()
                # Store OTP in the user model
                user.otp = str(otp_code)  # Convert to string to avoid type issues
                user.save()

                send_mail(
                    subject='Code',
                    message=f'Your OTP code is {otp_code}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user_email],
                    fail_silently=False,
                )
                messages.success(request, "OTP sent successfully. Please check your email.")
                return redirect('otp_verification', user.id)
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Fill the form correctly.")
    else:
        form = MyUserLoginForm()

    return render(request, 'login.html', {'form': form})

def verify_otp(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        # Fix: Compare as strings to avoid type mismatch
        if user_otp == user.otp:
            messages.success(request, "OTP verified successfully!")
            login(request, user)
            # Clear the OTP after successful verification
            user.otp = None
            user.save()
            return redirect('index')
        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('otp_verification', user_id=user_id)

    # Handle GET request by rendering the OTP verification form
    return render(request, 'otp_verification.html', {'user_id': user_id})

def resend_otp(request, user_id):
    user = User.objects.get(id=user_id)
    otp_code = generate_OTP_code()
    user.otp = str(otp_code)
    user.save()
    send_mail(
        subject='Code',
        message=f'Your OTP code is {otp_code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
    messages.success(request, "OTP resent successfully!")
    return redirect('otp_verification', user_id=user_id)


def user_logout_view(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect('index')