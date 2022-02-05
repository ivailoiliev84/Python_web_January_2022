from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('The field must contain only letters!')


