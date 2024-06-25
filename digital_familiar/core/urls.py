from django.urls import path

from .views import landing, profile

app_name = "core"

urlpatterns = [
    path("", landing, name="landing"),
    path("", profile, name="profile")
]