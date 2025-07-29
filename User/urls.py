from django.urls import path
from .views import *
from .views import user_register_view

urlpatterns=[
    path('signup/', user_register_view, name='signup'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('verify-otp/<int:user_id>/', verify_otp, name='otp_verification'),
    path('resend_otp/<int:user_id>/', resend_otp, name='resend_otp')
]
