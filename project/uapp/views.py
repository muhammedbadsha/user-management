import email
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('/')  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid')
            return redirect('login')
        
    else:
        return render(request,'login.html')



def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # password2 ='123'
        # password1 = '123'
        # username = 'badu'
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('passsword not matching')
            return redirect('register')
        # return redirect('/')
    else:
        return render(request,'register.html')

   
def logout(request):
    auth.logout(request)
    return redirect('login')
