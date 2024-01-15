from django.urls import path
from .views import register, campus_ambassador , home, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('register/<str:referral_code>/', register, name='register_with_referral'),
    path('campus-ambassador/', campus_ambassador, name='campus_ambassador'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),

    # Add other URLs as needed
]
