from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact


# Create your views here.

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def Christmas(req):
    return render(req, 'Christmas.html')

def contact(request):
     if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        Message=request.POST['Message']
        Contact.objects.create(Name=uname,email=email,phone=phone,Message=Message)
        # contact.save()
        return redirect('index')
     
     return render(request, 'contact.html')
        

       

           

def  Diwali(req):
    return render(req, 'Diwali.html')

def gallery(req):
    return render(req, 'gallery.html')

def independence(req):
    return render(req, 'independence.html')

def Newyear(req):
    return render(req, 'Newyear.html')

def others(req):
    return render(req, 'others.html')

def Republic(req):
    return render(req, 'Republic.html')

def service(req):
    return render(req, 'service.html')

def Login(request):
    if request.method=='POST':
        name=request.POST.get('Full Name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(name,uname,email,phone,pass1)
            my_user.save()
            return redirect('Login')
    return render(request, 'Login.html')

def signup(req):
    return render(req, 'signup.html')

def uiuxdesign(req):
    return render(req, 'uiuxdesign.html')

def digitalmarketing(req):
    return render(req, 'digitalmarketing.html')

def accounts(req):
    return render(req, 'accounts.html')

def mobileapp(req):
    return render(req, 'mobileapp.html')

def projectdesign(req):
    return render(req, 'projectdesign.html')

def websitedesign(req):
    return render(req, 'websitedesign.html')


def secretarialservice(req):
    return render(req, 'secretarialservice.html')

def otherservices(req):
    return render(req, 'otherservices.html')

def payrollservice(req):
    return render(req, 'payrollservice.html')

def accountingservice(req):
    return render(req, 'accountingservice.html')

def h1bvisa(req):
    return render(req, 'h1bvisa.html')



# def indexcopy(req):
#     return render(req, 'indexcopy.html')