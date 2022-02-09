from django.shortcuts import render, redirect

# Create your views here.
from petstagram.main_app.models import Pet, PetPhoto, Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    return render(request, 'main_app/home_page.html')


def dashboard(request):
    # pets = Pet.objects.all()
    profile = get_profile()

    pet_photos = set(PetPhoto.objects \
                     .prefetch_related('tagged_pet') \
                     .filter(tagged_pet__user_profile=profile))

    context = {

        'pet_photos': pet_photos,
    }

    return render(request, 'main_app/dashboard.html', context)


def profile_details(request):
    return render(request, 'main_app/profile_details.html')


def photo_details(request, pk):
    pet_photo = PetPhoto.objects\
        .prefetch_related('tagged_pet')\
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,

    }
    return render(request, 'main_app/photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.like += 1
    pet_photo.save()

    return redirect('photo details', pet_photo.pk)
