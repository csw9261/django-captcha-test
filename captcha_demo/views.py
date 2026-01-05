from django.shortcuts import render
from django.contrib import messages
from .forms import ReCaptchaForm, HCaptchaForm, TurnstileForm


def index(request):
    """메인 페이지 - 3가지 CAPTCHA 링크"""
    return render(request, "captcha_demo/index.html")


def recaptcha_view(request):
    """Google reCAPTCHA v2 테스트"""
    if request.method == "POST":
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, "reCAPTCHA 검증 성공!")
        else:
            messages.error(request, "reCAPTCHA 검증 실패. 다시 시도해주세요.")
    else:
        form = ReCaptchaForm()

    return render(request, "captcha_demo/recaptcha.html", {"form": form})


def hcaptcha_view(request):
    """hCaptcha 테스트"""
    if request.method == "POST":
        form = HCaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, "hCaptcha 검증 성공!")
        else:
            messages.error(request, "hCaptcha 검증 실패. 다시 시도해주세요.")
    else:
        form = HCaptchaForm()

    return render(request, "captcha_demo/hcaptcha.html", {"form": form})


def turnstile_view(request):
    """Cloudflare Turnstile 테스트"""
    if request.method == "POST":
        form = TurnstileForm(request.POST)
        if form.is_valid():
            messages.success(request, "Turnstile 검증 성공!")
        else:
            messages.error(request, "Turnstile 검증 실패. 다시 시도해주세요.")
    else:
        form = TurnstileForm()

    return render(request, "captcha_demo/turnstile.html", {"form": form})
