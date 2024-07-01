from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CharacterCreateForm, CharacterEditForm, PartyCreateForm, PartyEditForm
from .models import Character, Party, Profile

# Registration views
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Page views
def home_page(request):
    if request.user.is_authenticated:
        profile = request.user.pk
        #return render(request, "core/profile.html")
        return redirect("profile", pk=profile)
    else:
        return render(request, "core/landing.html")
    
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    my_characters = Character.objects.filter(character_owner=request.user)
    my_parties = Party.objects.filter(party_owner=request.user)
    parties_memberof = profile.parties.all()
    return render(request, "core/profile.html", 
                  {"profile" : profile, 
                   "my_characters" : my_characters, 
                   "my_parties" : my_parties, 
                   "parties_memberof" : parties_memberof})

# Character views
def character_sheet(request, pk): 
    character = Character.objects.get(pk=pk)
    return render(request, "core/character_sheet.html", {"character" : character})

def character_create(request):
    if request.method == "POST":
        form = CharacterCreateForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.character_owner = request.user
            character.save()
            return redirect("character_sheet", pk=character.pk)      
    else:
        form = CharacterCreateForm()
    return render(request, "core/character_create.html", {"form" : form})
    
def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        form = CharacterCreateForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.save()
            return redirect("character_sheet", pk=character.pk)      
    else:
        form = CharacterCreateForm(instance=character)
    return render(request, "core/character_edit.html", 
                  {"form" : form, 
                   "character": character})
    
def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == "POST":
        character.delete()
        profile = request.user.pk
        return redirect("profile", pk=profile)
    
    return render(request, "core/character_delete.html", {"character": character})

# Party views
def party_hub(request, pk): 
    party = Party.objects.get(pk=pk)
    party_members = party.members.all()
    return render(request, "core/party_hub.html", 
                  {"party" : party,
                   "party_members" : party_members})

def party_create(request):
    if request.method == "POST":
        form = PartyCreateForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.party_owner = request.user
            party.save()
            return redirect("party_hub", pk=party.pk)      
    else:
        form = PartyCreateForm()
    return render(request, "core/party_create.html", {"form" : form})
    
def party_edit(request, pk):
    party = get_object_or_404(Party, pk=pk)
    if request.method == "POST":
        form = PartyCreateForm(request.POST, instance=party)
        if form.is_valid():
            party = form.save(commit=False)
            party.save()
            return redirect("party_hub", pk=party.pk)      
    else:
        form = PartyCreateForm(instance=party)
    return render(request, "core/party_edit.html", {"form" : form, "party": party})
    
def party_delete(request, pk):
    party = get_object_or_404(Party, pk=pk)
    if request.method == "POST":
        party.delete()
        profile = request.user.pk
        return redirect("profile", pk=profile)
    
    return render(request, "core/party_delete.html", {"party": party})

def party_join(request, pk):
    party = get_object_or_404(Party, pk=pk)
    if request.method == "POST":
        party.members.add(request.user.profile)
        return redirect("party_hub", pk=party.pk)

    return render(request, "core/party_join.html", {"party": party})

def party_leave(request, pk):
    party = get_object_or_404(Party, pk=pk)
    party.members.remove(request.user.profile)
    return redirect("party_hub", pk=party.pk)


    
        