from django.shortcuts import redirect, render

from petstagram.main_app.forms import PetPhotoCreateForm, PetPhotoUpdateForm
from petstagram.main_app.models import PetPhoto


def create_photo(request):
    if request.method == 'POST':
        form = PetPhotoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PetPhotoCreateForm()
    context = {
        'form': form
    }
    return render(request, 'main_app/pet_photos_template/photo_create.html', context)


def edit_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetPhotoUpdateForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = PetPhotoUpdateForm(instance=photo)
    context = {
        'form': form,
        'photo': photo
    }
    return render(request, 'main_app/pet_photos_template/photo_edit.html', context)


def photo_details(request, pk):
    pet_photo = PetPhoto.objects \
        .prefetch_related('tagged_pet') \
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,

    }
    return render(request, 'main_app/pet_photos_template/photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.like += 1
    pet_photo.save()

    return redirect('photo details', pet_photo.pk)
