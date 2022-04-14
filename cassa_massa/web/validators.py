from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha() or not ch.isspace():
            raise ValidationError('Name must contain only letters')