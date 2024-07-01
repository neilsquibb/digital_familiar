from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Character, Party

# Auth forms
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

# Character forms
class CharacterCreateForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ("character_name", )

class CharacterEditForm(forms.ModelForm):
    
    class Meta:
        model = Character
        fields = ("character_name", )

# Party forms
class PartyCreateForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = ("party_name", )

class PartyEditForm(forms.ModelForm):
    
    class Meta:
        model = Party
        fields = ("party_name", )