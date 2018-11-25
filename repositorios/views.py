# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

#Probando Ajax
from django.http import JsonResponse

#Remote Shell
#import pexpect.pxssh as pxssh
#import getpass
import base64
import paramiko

# Create your views here.


#
from repositorios.models import PrototypeeModel


@login_required
def home(request):
    #objs = PrototypeeModel.objects.all()
    #print(request.session.keys())
    #print(request.user)
    
    #{'username': request.session['username']}
    return render(request, "repositorios/index.html",{"username": request.user.username})#,{'data' : objs})


@login_required
def conexion(request):
    return render(request, "", {})

@login_required
def consultar(request):
    if request.method == 'POST':
	    comando = request.POST.get('command')
	    username = request.user.username
	    print('********************** ----> ', request.user.password)
	    usr = User.objects.get(username=username)
	    client = paramiko.SSHClient()
	    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    client.connect('192.168.56.103', 
			username=usr.username, password=request.COOKIES['code'])
	    
	    print('------------------------------ #### ', request.COOKIES.get('code',None))
	    stdin, stdout, stderr = client.exec_command(comando)
	    l = [] 
	    for line in stdout:
		l.append(line.strip('\n'))

	    client.close()
	    #try:                                                            
		    #s = pxssh.pxssh()
		    #hostname = raw_input('hostname: ')
		    #username = raw_input('username: ')
		    #password = getpass.getpass('12345')
		    #print(password)
		    #s.login ('jaime-pc', 'jaime', '12345')
		    #s.sendline ('uptime')   # run a command
		    #s.prompt()             # match the prompt
		    #print s.before          # print everything before the prompt.
		    #s.sendline ('ls -l')
		    #s.prompt()
		    #print s.before
		    #s.sendline ('df')
		    #s.prompt()
		    #print s.before
		    #s.logout()
	    #except pxssh.ExceptionPxssh, e:
		    #print "pxssh failed on login."
		    #print str(e)
	    data = {"data":l}
	    return JsonResponse(data)
    #return render(request, 'repositorios/show_commands.html', {'data': l})
    #return HttpResponse("<h1>Database Conecction </h1>")



