import datetime

from django.core.exceptions import ValidationError


def validator_only_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('The field must contain only letters!')


def validator_file_max_size_in_mb(max_size):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))

    return validate_image


def date_range_validator(value):
    start_date = datetime.date(1920, 1, 1)
    end_data = datetime.datetime.now()
    if start_date < value < end_data:
        raise ValidationError("Incorrect data")
    return value

