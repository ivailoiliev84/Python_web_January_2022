from django.shortcuts import redirect, render

from petstagram.main_app.forms import ProfileCreateForm, ProfileUpdateForm
from petstagram.main_app.models import PetPhoto, Profile, Pet
from petstagram.main_app.views.generic_views import get_profile


def profile_details(request):
    profile = get_profile()
    pets = Pet.objects.all()

    profile_photos = len(PetPhoto.objects.filter(tagged_pet__user_profile=profile).distinct())
    pet_photo_like = sum(pp.like for pp in PetPhoto.objects.filter(tagged_pet__user_profile=profile).distinct())

    context = {
        'profile': profile,
        'profile_photos': profile_photos,
        'pet_photo_like': pet_photo_like,
        'pets': pets,

    }
    return render(request, 'main_app/profile_template/profile_details.html', context)


def create_profile(request):
    user_profile = get_profile()
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'user_profile': user_profile,
    }

    return render(request, 'main_app/profile_template/profile_create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form,

    }
    return render(request, 'main_app/profile_template/profile_edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    else:
        return render(request, 'main_app/profile_template/profile_delete.html')
