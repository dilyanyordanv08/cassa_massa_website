from django.core.exceptions import ValidationError


def validate_only_letters_and_spaces(value):
    for ch in value:
        if not ch.isalpha() and not ch.isspace():
            raise ValidationError('Name must contain only letters')