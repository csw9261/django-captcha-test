from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from hcaptcha.fields import hCaptchaField
from turnstile.fields import TurnstileField


class ReCaptchaForm(forms.Form):
    """Google reCAPTCHA v2 폼"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class HCaptchaForm(forms.Form):
    """hCaptcha 폼"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    captcha = hCaptchaField()


class TurnstileForm(forms.Form):
    """Cloudflare Turnstile 폼"""
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    captcha = TurnstileField()
