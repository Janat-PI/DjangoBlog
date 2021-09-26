from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your successfully registration')
            return redirect('login')
        else:
            messages.error(request, 'Your errors registration')
    else:
        form = UserCreationForm()

    return render(request, template_name='register.html', context={'form': form})


def login(request):
    return render(request, template_name='login.html')