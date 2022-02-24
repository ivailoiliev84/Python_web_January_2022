from django.shortcuts import render

from petstagram.main_app.models import PetPhoto, Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    user_profile = get_profile()
    context = {
        'user_profile': user_profile
    }
    return render(request, 'main_app/home_page.html', context)


def dashboard(request):
    user_profile = get_profile()

    pet_photos = PetPhoto.objects \
        .prefetch_related('tagged_pet') \
        .filter(tagged_pet__user_profile=user_profile).distinct()

    context = {

        'pet_photos': pet_photos,
    }

    return render(request, 'main_app/dashboard.html', context)
