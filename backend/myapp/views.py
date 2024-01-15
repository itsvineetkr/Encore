from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, CampusAmbassadorForm
from .models import Referral, UserProfile





def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', {'user': request.user})

def campus_ambassador(request):
    if request.method == 'POST':
        form = CampusAmbassadorForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = CampusAmbassadorForm(instance=request.user.profile)
    return render(request, 'campus_ambassador.html', {'form': form})


def register(request, referral_code=None):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Check if a referral code was provided
            if referral_code:
                try:
                    referral = Referral.objects.get(code=referral_code)
                    user.profile.referral_code = referral_code
                    user.profile.save()
                    messages.success(request, 'Referral code applied successfully!')
                except Referral.DoesNotExist:
                    messages.error(request, 'Invalid referral code.')

            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form, 'referral_code': referral_code})

def generate_referral_code(user):
    import random
    import string

    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    Referral.objects.create(code=code, referred_user=user)

def campus_ambassador(request):
    if request.method == 'POST':
        form = CampusAmbassadorForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = CampusAmbassadorForm(instance=request.user.profile)
    
    # Check if the user has a referral code
    if not request.user.profile.referral_code:
        generate_referral_code(request.user)

    return render(request, 'campus_ambassador.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


# Create your views here.
