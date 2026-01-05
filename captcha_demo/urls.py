from django.urls import path
from . import views

app_name = "captcha_demo"

urlpatterns = [
    path("", views.index, name="index"),
    path("recaptcha/", views.recaptcha_view, name="recaptcha"),
    path("hcaptcha/", views.hcaptcha_view, name="hcaptcha"),
    path("turnstile/", views.turnstile_view, name="turnstile"),
]
