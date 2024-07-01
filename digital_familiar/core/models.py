from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# User models
"""CustomUser built inheriting from Django built in User. Keeps authorization 
and personal info"""
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
# Page models
"""Profile that has one-to-one with CustomUser. Instance deletes when 
CustomUser instance is deleted. Keeps non-auth info and connections"""
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    parties = models.ManyToManyField("Party", related_name="members", symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
    
# Creates profile attached to each new user
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=CustomUser)

"""Character has many-to-one relationship with Profile. Instance deletes 
when Profile instance is deleted."""
class Character(models.Model):
    character_owner = models.ForeignKey(CustomUser, related_name="characters", on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)

    def __str__(self):
        return self.character_name
    
"""Party has many-to-one relationship with Profile. Instance deletes 
when Profile instance is deleted."""
class Party(models.Model):
    party_owner = models.ForeignKey(CustomUser, related_name="parties", on_delete=models.CASCADE)
    party_name = models.CharField(max_length=100)

    def __str__(self):
        return self.party_name

