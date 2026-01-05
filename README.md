# Django CAPTCHA Test

Django에서 사용 가능한 CAPTCHA 라이브러리 비교 테스트 프로젝트

## 테스트 대상 CAPTCHA

| CAPTCHA | 라이브러리 | 특징 |
|---------|-----------|------|
| **reCAPTCHA v2** | django-recaptcha | Google 제공, 가장 널리 사용됨 |
| **hCaptcha** | django-hcaptcha | 프라이버시 중심, GDPR 준수 |
| **Turnstile** | django-turnstile | Cloudflare 제공, 사용자 친화적 |

## 설치 및 실행

```bash
# 1. 프로젝트 디렉토리 이동
cd django-captcha-test

# 2. 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 서버 실행
python manage.py runserver 8080
```

브라우저에서 http://127.0.0.1:8080/ 접속

## 프로젝트 구조

```
django-captcha-test/
├── config/                 # Django 설정
│   ├── settings.py         # CAPTCHA 키 설정 포함
│   └── urls.py
├── captcha_demo/           # 데모 앱
│   ├── forms.py            # 3가지 CAPTCHA 폼
│   ├── views.py            # 폼 처리 뷰
│   ├── urls.py
│   └── templates/
└── requirements.txt
```

## CAPTCHA 설정 (settings.py)

현재 테스트 키 사용 중 (항상 통과):

```python
# reCAPTCHA
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

# hCaptcha
HCAPTCHA_SITEKEY = "10000000-ffff-ffff-ffff-000000000001"
HCAPTCHA_SECRET = "0x0000000000000000000000000000000000000000"

# Turnstile
TURNSTILE_SITEKEY = "1x00000000000000000000AA"
TURNSTILE_SECRET = "1x0000000000000000000000000000000AA"
```

## 실제 키 발급

| 서비스 | 발급 URL |
|--------|----------|
| reCAPTCHA | https://www.google.com/recaptcha/admin |
| hCaptcha | https://dashboard.hcaptcha.com/signup |
| Turnstile | https://dash.cloudflare.com |

## CAPTCHA 비교

| | reCAPTCHA | hCaptcha | Turnstile |
|---|---|---|---|
| 제공사 | Google | Intuition Machines | Cloudflare |
| 사용자 경험 | 체크박스 + 가끔 이미지 | 체크박스 + 가끔 이미지 | 대부분 자동 통과 |
| 프라이버시 | 데이터 수집 | GDPR 준수 | 데이터 수집 안 함 |
| 가격 | 무료 (제한 있음) | 무료 티어 | 완전 무료 |

## 장단점

### reCAPTCHA v2

**장점**
- 가장 오래되고 검증된 솔루션
- 방대한 문서와 커뮤니티 지원
- 높은 봇 탐지 정확도
- v3 (invisible) 버전도 지원

**단점**
- Google에 사용자 데이터 전송 (프라이버시 우려)
- 중국에서 차단됨
- 이미지 챌린지가 때때로 어려움
- 월 100만 건 초과 시 유료

---

### hCaptcha

**장점**
- GDPR, CCPA 등 프라이버시 규정 준수
- Google 의존성 없음
- Cloudflare 등 대형 서비스에서 채택
- 접근성 옵션 제공

**단점**
- reCAPTCHA보다 인지도 낮음
- 이미지 챌린지 빈도가 높은 편
- 무료 티어 제한 있음

---

### Turnstile

**장점**
- 대부분 사용자 상호작용 불필요 (자동 통과)
- 완전 무료 (사용량 제한 없음)
- 프라이버시 보호 (데이터 수집 안 함)
- 가장 빠른 사용자 경험
- 접근성 우수

**단점**
- reCAPTCHA 대비 레퍼런스 적음
- Cloudflare 계정 필요

---

## 추천

| 상황 | 추천 |
|------|------|
| 신규 프로젝트 | **Turnstile** - 무료, UX 최고 |
| GDPR 준수 필요 | **hCaptcha** 또는 **Turnstile** |
| 검증된 솔루션 필요 | **reCAPTCHA** |
| 중국 사용자 대상 | **hCaptcha** 또는 **Turnstile** |
