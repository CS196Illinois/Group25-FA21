from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from Dashboard.models import User, Macro
from .forms import CreateUserForm
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
import time


# Create your views here.

def loginPage(request):

    if request.user.is_authenticated:
        return render(request, 'index.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'succesfully logged in')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Account Successfully Created!')
    context = {'form': form}
    return render(request, 'register.html', context)


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'login.html')


def diet(request):
    if request.user.is_authenticated:
        return render(request, 'diet.html')
    else:
        return render(request, 'login.html')


def exercise(request):
    if request.user.is_authenticated:
        return render(request, 'exercise.html')
    else:
        return render(request, 'login.html')


def form(request):
    if request.user.is_authenticated:
        return render(request, 'form.html')
    else:
        return render(request, 'login.html')


def sleep(request):
    if request.user.is_authenticated:
        return render(request, 'sleep.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        print("not logged in")
