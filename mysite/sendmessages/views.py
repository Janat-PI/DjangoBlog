from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages


def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'janat200066@gmail.com',
                      ['janat200066@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Письмо отправленно')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'что-то не то, еще раз напиши!')
    else:
        form = ContactForm()
    return render(request, template_name='test.html', context={'form': form})