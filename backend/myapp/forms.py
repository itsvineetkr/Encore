
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile


class UserRegistrationForm(UserCreationForm):
    college_name = forms.CharField(max_length=100)
    year = forms.IntegerField()
    dob = forms.DateField()
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    referral_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'college_name', 'year', 'dob', 'phone', 'email', 'password1', 'password2', 'referral_code']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)



class CampusAmbassadorForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    referral_code = forms.CharField(max_length=10)

    def clean_referral_code(self):
        referral_code = self.cleaned_data.get('referral_code')
        # Perform referral code validation here
        if referral_code != 'correct_referral_code':
            raise forms.ValidationError('Invalid referral code')
        return referral_code

    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'referral_code', 'is_campus_ambassador']






