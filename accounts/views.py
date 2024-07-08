from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages,auth
from contacts.models import Contact
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Agent
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request , 'Email Name Already Exits ')
                return redirect('accounts:register')
            else:
                user = form.save()
                login(request, user)
                agent = Agent.objects.create(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email)                                
                messages.success(request, ("Account created"))
                return redirect('pages:index')
                # send email
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, settings.EMAIL_HOST_USER]
                send_mail(
                    'Become a Boma yangu agent', #subject
                    'Dear {user.username}, thank you for registering to become a boma agent officer. We will contact you for further vetting.', # message
                    'settings.EMAIL_HOST_USER', #from email
                    ['user.email','settings.EMAIL_HOST_USER', user.email],
                    fail_silently= False # to email
                    )
        else:
            messages.error(request, ("ERROR!! Check requirements"))
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html', {'form': form})


'''

    if request.method == 'POST':
        if password == password2:
            if User.objects.filter(username=username).exists():
                    messages.error(request , 'User Name Already Taken')
                    return redirect('accounts:register_view')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request , 'Email Name Already Exits ')
                    return redirect('accounts:register_view')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name
                        =last_name)
                    # auth.login(request , user)
                    # messages.success(request,'You Are Now LoggedIn')
                    # return redirect('pages:index')
                    user.save()
                    login(request, user)
                    Agent = Agent.objects.create(username=user.username,first_name=first_name,last_name
                        =last_name, created_by=user)
                    messages.success(request,'You Are Now Registered')
                    subject = 'welcome to Boma'
                    message = f'Dear {user.username}, thank you for registering to become a boma agent officer. We will contact you for further vetting.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email,]
                    send_mail((subject, message, email_from, recipient_list), fail_silently=False)              
                    return redirect('accounts:login_view')
                    
        else:
            messages.error(request , 'Password Doest Not Match')
            return redirect('accounts:register_view')

    else:
        return render(request,'accounts/register.html')
'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username , password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You Are Now LoggedIn')
            return redirect('accounts:dashborad')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('accounts:login_view')
    else:
        return render(request,'accounts/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,'You Are Now Logged Out')
    return redirect('pages:index')

def dashborad(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    return render(request,'accounts/dashborad.html',{'contacts' : user_contact})
