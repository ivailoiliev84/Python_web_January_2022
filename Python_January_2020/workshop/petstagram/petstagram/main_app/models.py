from django.db import models
from django.core.validators import MinLengthValidator

from petstagram.main_app.validators import validator_only_letters, validator_file_max_size_in_mb

"""
The user must provide the following information in their profile:
    • The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
    • The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
    • Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:
    • Date of birth: day, month, and year of birth.
    • Description - a user can write any description about themselves, no limit of words/chars.
    • Email - a user can only write a valid email address.
    • Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
"""


# Create your models here.


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'
    GENDER = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_only_letters,

        )

    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validator_only_letters,
        )
    )

    profile_picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    # GENDER_CHOICE = (
    #     ("Male", "Male"),
    #     ("Female", "Female"),
    #     ("Do not show", "Do not show"),
    # )
    gender = models.CharField(
        max_length=max(len(x) for (x, _) in GENDER),
        choices=GENDER,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


"""The user must provide the following information when adding a pet in their profile:
    • Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
    • Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
The user may provide the following information when adding a pet to their profile:
    • Date of birth - pet's day, month, and year of birth."""


class Pet(models.Model):
    PET_NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPE_CHOICE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=PET_NAME_MAX_LENGTH,
        unique=Profile
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPE_CHOICE),
        choices=TYPE_CHOICE,

    )

    day_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return f'{self.type} {self.name}'


"""The user must provide the following information when uploading a pet's photo in their profile:
    • Photo - the maximum size of the photo can be 5MB
    • Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
The user may provide the following information when uploading a pet's photo in their profile:
    • Description - a user can write any description about the picture, with no limit of words/chars
Other:
    • Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
    • Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited."""


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            validator_file_max_size_in_mb,
        )

    )
    tagged_pet = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
    )

    like = models.IntegerField(
        default=0,
    )





