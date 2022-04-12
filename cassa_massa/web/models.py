from django.core.validators import MinLengthValidator
from django.db import models

from cassa_massa.web.validators import validate_only_letters


class Contact(models.Model):
    NAME_MAX_LENGTH = 25
    CELL_PHONE_MAX_LENGTH = 10
    CELL_PHONE_MIN_LENGTH = 10
    EMAIL_SUBJECT_MAX_LENGTH = 100
    EMAIL_MESSAGE_MAX_LENGTH = 1000

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    cell_phone_number = models.CharField(
        max_length=CELL_PHONE_MAX_LENGTH,
        validators=(
            MinLengthValidator(CELL_PHONE_MIN_LENGTH),
            validate_only_letters,
        ),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    subject = models.CharField(
        max_length=EMAIL_SUBJECT_MAX_LENGTH,
    )
    message = models.TextField(
        max_length=EMAIL_MESSAGE_MAX_LENGTH,
    )

    def __str__(self):
        return self.email
