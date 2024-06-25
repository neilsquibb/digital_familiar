from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .forms import CustomUserCreationForm

# Registration views
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Page views
def home_page(request):
    if request.user.is_authenticated:
        return render(request, "core/profile.html")
    else:
        return render(request, "core/landing.html")
