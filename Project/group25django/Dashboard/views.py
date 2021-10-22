from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from Dashboard.models import User
from .forms import CreateUserForm
from django.contrib import messages
import time
# Create your views here.

# return the home page
def home(request):
    return render(request, 'index.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def diet(request):
    return render(request, 'diet.html')
def exercise(request):
    return render(request, 'exercise.html')
def form(request):
    return render(request, 'form.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Account Successfully Created!')
    context = {'form':form}
    return render(request, 'register.html', context)
def sleep(request):
    return render(request, 'sleep.html')