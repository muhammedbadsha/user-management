import email
from multiprocessing import context
from urllib import request
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect, render



# Create your views here.

def admin_home(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        print(user)
        context={'user': user}
        return render(request, 'adminpanel/admin_home.html',context)

      #  return render(request, 'adminpanel/admin_home.html')
    else:
        return redirect('admin_login')

def admin_login(request):
   if request.user.is_authenticated:
       return redirect('admin_home')
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username,password=password)
       if user is not None:
           if user.is_superuser:
               auth.login(request,user)
               return redirect('admin_home')
           else:
               messages.info(request,'no admin that name')
               return redirect(admin_login)
       else:
            messages.info(request,'enter username and password')
            return redirect(admin_login)
   else:
       return render(request, 'adminpanel/admin_login.html')




def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')

def viewuser(request,id):
    user = User.objects.get(id=id)
    context ={'user':user}
    return render(request,'adminpanel/viewTemplate.html',context)

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('admin_home')

def adduser(request):

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
                return redirect('adduser')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('adduser')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print('user created')
                return redirect('admin_home')
        else:
            print('passsword not matching')
            return redirect('adduser')
        # return redirect('/')
    else:
        return render(request,'adminpanel/adduser.html')


def searchuser(request):
    username = request.POST['username']
    user = User.objects.get(username= username)
    context = {'user':user}
    return render(request,'adminpanel/search.html',context)
    

def adminupdate(request,id):
    user = User.objects.get(id=id)
    context ={'user':user}
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user.username=username
        user.email=email
        user.set_password(password)
        user.save()
        return redirect(admin_home)
    return render(request,'adminpanel/adminupdate.html', context)