from django.urls import path, include

from .views import character_create, character_delete, character_edit, character_sheet, party_create, party_delete, party_edit, party_hub, party_join, party_leave, home_page, profile, SignUpView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", home_page, name="home_page"),
    path("profile/<int:pk>/", profile, name="profile"),
    path("character/<int:pk>/", character_sheet, name="character_sheet"),
    path("character/create/", character_create, name="character_create"),
    path("character/<int:pk>/edit/", character_edit, name="character_edit"),
    path("character/<int:pk>/delete/", character_delete, name="character_delete"),
    path("party/<int:pk>/", party_hub, name="party_hub"),
    path("party/create/", party_create, name="party_create"),
    path("party/<int:pk>/edit/", party_edit, name="party_edit"),
    path("party/<int:pk>/delete/", party_delete, name="party_delete"),
    path("party/<int:pk>/join/", party_join, name="party_join"),
    path("party/<int:pk>/leave", party_leave, name="party_leave"),
]