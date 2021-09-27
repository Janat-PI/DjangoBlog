from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class ContactForm(forms.Form):
    subject = forms.CharField(label='subject', widget=forms.TextInput())
    content = forms.CharField(label='text', widget=forms.TextInput(attrs={'rows': 5}))
    captcha = CaptchaField()