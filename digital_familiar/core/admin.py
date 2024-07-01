from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Character, Party

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Makes the CustomUser and Profile editable together in the admin
class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Makes the SustomUser and Profile editable together in the admin
    inlines = [ProfileInline]
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Character)
admin.site.register(Party)