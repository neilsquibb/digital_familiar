from django.urls import path, include

from .views import home_page, SignUpView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", home_page, name="home_page"),
]