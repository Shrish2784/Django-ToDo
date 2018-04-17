from django.shortcuts import render, redirect
from ToDoApp import models
from django.conf import settings
from ToDoApp.forms import (
    signup_form,
    edit_profile_form
)
from django.contrib.auth.views import login
from django.contrib.auth.forms import (
    PasswordChangeForm,
    PasswordResetForm
)
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'ToDoApp/index.html')

# @login_required(login_url=settings.LOGIN_URL)
def home(request):
    todos = models.ToDo.objects.all()
    context_dict = {
        'todos': todos,
    }
    return render(request, 'ToDoApp/home.html', context=context_dict)

def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            context_dict = {
                'form': form,
            }
            return render(request, 'ToDoApp/signup.html', context=context_dict)
    else:
        form = signup_form()
        context_dict = {
            'form': form,
        }
        return render(request, 'ToDoApp/signup.html', context=context_dict)

# @login_required(login_url=settings.LOGIN_URL)
def profile(request):
    user = request.user
    context_dict = {
        'profile': user,
    }
    return render(request, 'ToDoApp/profile.html', context=context_dict)

# @login_required(login_url=settings.LOGIN_URL)
def edit_profile(request):
    if request.method == 'POST':
        form = edit_profile_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:
            context_dict = {
                'form': form
            }
            return render(request, 'ToDoApp/edit_profile.html', context=context_dict)
    else:
        form = edit_profile_form(instance=request.user)
        context_dict = {
            'form': form
        }
        return render(request, 'ToDoApp/edit_profile.html', context=context_dict)

# @login_required(login_url=settings.LOGIN_URL)
def edit_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            return redirect('/profile')
        else:
            context_dict = {
                'form': form
            }
            return render(request, 'TodoApp/edit_password.html', context=context_dict)
    else:
        form = PasswordChangeForm(user=request.user)
        context_dict = {
            'form': form
        }
        return render(request, 'ToDoApp/edit_password.html', context=context_dict)
