from django import forms

from petstagram.main_app.models import Profile, Pet, PetPhoto


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'profile_picture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL'}),

        }


class ProfileUpdateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user_profile',)

        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Enter email'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter descriptions', 'row': 3})
        }


class PetCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'day_of_birth',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'}),

        }


class PetUpdateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'day_of_birth',)


class PetPhotoCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pet',)


class PetPhotoUpdateForm(forms.ModelForm):
    class Meat:
        model = PetPhoto
        fields = ('description', 'tagged_pet',)
