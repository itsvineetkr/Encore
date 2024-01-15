from django.conf import settings
import hmac
import hashlib
import base64
import json
from django.http import HttpResponse
from models import Reg_User
from django.shortcuts import redirect,HttpResponseRedirect,render_to_response

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or any other page
        else:
            # Handle invalid login credentials
            return render(request, 'login/login.html', {'error': 'Invalid credentials'})
    return render(request, 'login/login.html')


    if sig != expected_sig:
        return render_to_response('error.html')

    else:
        try:
            user = Reg_User.objects.get(name=data['registration']['name'],email=data['registration']['email'])
            return HttpResponseRedirect('//www.Encore.com')
        except:
            user = Reg_User()
            user.name = data['registration']['name']
            user.contact = data['registration']['contact']
            user.college = data['registration']['college']
            user.gender = data['registration']['gender']
            user.birthday = data['registration']['birthday']
            user.location = data['registration']['location']['name']
            user.email = data['registration']['email']
            user.fb_ID = data['user_id']
            user.save()
            return HttpResponseRedirect('//www.Encore.com')





def event-register(request):
	if request.method == 'POST':
		registration = EventRegistration()
		registration.team_name = request.POST['team_name']
		registration.team_representative = request.POST['team_representative']
		registration.representative_contact = request.POST['representative_contact']
		registration.branch = request.POST['branch']
		registration.email = request.POST['email']
		registration.event = request.POST['event']
		registration.member_2_details = request.POST['member_2_details']
		registration.member_3_details = request.POST['member_3_details']
		registration.member_4_details = request.POST['member_4_details']
		registration.member_5_details = request.POST['member_5_details']
		registration.save()
		return HttpResponseRedirect('//www.Encore.com/')

	else:
		return HttpResponseRedirect('//www.Encore.com/')
