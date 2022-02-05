from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile, Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
