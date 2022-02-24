from django.shortcuts import redirect, render

from petstagram.main_app.forms import PetCreateForm, PetUpdateForm
from petstagram.main_app.models import Pet
from petstagram.main_app.views.generic_views import get_profile


def create_pet(request):
    profile = get_profile()
    if request.method == 'POST':
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user_profile = profile
            pet.save()
            return redirect('profile details')

    else:
        form = PetCreateForm()
    contex = {
        'form': form
    }
    return render(request, 'main_app/pet_template/pet_create.html', contex)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'POST':
        form = PetUpdateForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = PetUpdateForm(instance=pet)
    context = {
        'form': form,
        'pet': pet

    }
    return render(request, 'main_app/pet_template/pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        form = PetCreateForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()
            return redirect('profile details')

    else:
        form = PetUpdateForm(instance=pet)
    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'main_app/pet_template/pet_delete.html', context)
