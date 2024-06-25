from django.shortcuts import render

def landing(request):
    if request.user.is_authenticated:
        return render(request, "core/profile.html")
    else:
        return render(request, "core/landing.html")

def profile(request):
    if request.user.is_authenticated:
        return render(request, "core/profile.html")
    else:
        return render(request, "core/landing.html")
