from django.shortcuts import render
from .form import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            fname = request.POST.get('first_name','')
            lname = request.POST.get('last_name','')
            unmae = request.POST.get('user_name','')
            pwd = request.POST.get('password','',)
            email = request.POST.get('email','')
            mob = request.POST.get('number','')

            data=RegistrationData(
                first_name=fname,
                last_name=lname,
                user_name=unmae,
                password=pwd,
                email=email,
                number=mob,


            )

            data.save()
            iform = LoginForm()
            return render(request,'reglogin_login.html',{'iform':iform})
    else:
        rform = RegistrationForm()
        return render(request,'reglogin_reg.html',{'rform':rform})



def login_view(request):
    if request.method == "POST":
        iform = LoginForm(request.POST)
        if iform.is_valid():
            user = request.POST.get('user_name','')
            password = request.POST.get('password','')

            un = RegistrationData.objects.filter(user_name=user)
            pwd = RegistrationData.objects.filter(password=password)

            if  un and pwd:
                return HttpResponse('invalid details')
            else:
                return HttpResponse('valid details')
    else:
        iform =LoginForm()
        return render(request,'reglogin_login.html',{'iform':iform})







