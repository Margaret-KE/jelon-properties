from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Create your views here.
def home(request):
	return render (request, 'index.html')

# signup page
def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Account created"))
            return redirect('home')
        else:
            messages.success(request, ("ERROR!! Check requirements"))
            return redirect("user_signup")
    else:
        return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            messages.success(request, ("You have been logged In!!"))

        else:
            return redirect('user_login')
            messages.success(request, ("ERROR!!"))
    else:
        return render(request, 'login.html', {})

# logout page
def user_logout(request):
    logout(request)
    return redirect('home')
    messages.success(request, ("You have been logged out"))


def property(request):
	return render(request , 'property-grid.html')

def property_single(request):
	return render(request, 'property-single.html')

def contact(request):
	return render(request, 'contact.html')

def blog_grid(request):
	return render(request, 'blog-grid.html')

def blog_single(request):
	return render(request, 'blog-single.html')

def agent_single(request):
	return render(request, 'agent-single.html')

def agents_grid(request):
	return render(request, 'agents-grid.html')