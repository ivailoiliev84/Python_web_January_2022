from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile, Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    """
        admin.StackedInline and model
    """
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
       add pet visualisation under
       profile visualisation in admin
    """

    inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name', 'gender')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'user_profile')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
