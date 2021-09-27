from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login,  logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your successfully registration')
            return redirect('index')
        else:
            messages.error(request, 'Your errors registration')
    else:
        form = UserRegisterForm()

    return render(request, template_name='register.html', context={'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()

    return render(request, template_name='login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')