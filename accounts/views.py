# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from forms import LoginForm
#from accounts.backend import MyBackend
from django.contrib.auth import backends, get_user_model
from django.db.models import Q

# Create your views here.

from django.shortcuts import render

def login(request):
    return render(request, "index.html", {})

def loginpam(request):
    print(len(request.POST))
    username = 'jaime'
    password = '12345'
    user = authenticate(username=username, password = password, servicio='login')
    if user:
	print('User logged!')
    else:
	print('user not found')
	


def session_demo(request):
    username = None  # default value
    form_login = LoginForm()
    if request.method == 'GET':

        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('demos-sessions')

        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())  # session lifetime in seconds(from now)
            print(
                request.session.get_expiry_date())  # datetime.datetime object which represents the moment in time at which the session will expire

    elif request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            print('Datos correctos!')
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            if username.strip() == 'youtuber' and password.strip() == 'secret':
                request.session['username'] = username
                print('Cookies?')
                print(request)
            else:
                username = None
        else:
            print('Datos incorrectos!')

    return render(request, 'accounts/index.html', {
        'demo_title': 'Sessions in Django',
        'form': form_login,
        'username': username,
    })
