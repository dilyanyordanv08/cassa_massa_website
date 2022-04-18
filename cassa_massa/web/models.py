from django.core.validators import MinLengthValidator
from django.db import models
from cassa_massa.web.validators import validate_only_letters_and_spaces


class Contact(models.Model):
    NAME_MAX_LENGTH = 25
    CELL_PHONE_MAX_LENGTH = 10
    CELL_PHONE_MIN_LENGTH = 10
    EMAIL_SUBJECT_MAX_LENGTH = 100
    EMAIL_MESSAGE_MAX_LENGTH = 1000

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validate_only_letters_and_spaces,
        )
    )
    cell_phone_number = models.CharField(
        max_length=CELL_PHONE_MAX_LENGTH,
        validators=(
            MinLengthValidator(CELL_PHONE_MIN_LENGTH),
        )
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


class Services(models.Model):
    SERVICES_NAME_MAX_LENGTH = 35

    name = models.CharField(
        max_length=SERVICES_NAME_MAX_LENGTH,
        validators=(
            validate_only_letters_and_spaces,
        )
    )

    image = models.ImageField()

    description = models.TextField(

    )

    def __str__(self):
        return self.name


class FinishedProducts(models.Model):
    TABLE_NAME_MAX_LENGTH = 40
    TABLE_SIZES_MAX_LENGTH = 30

    table_image = models.ImageField()

    table_name = models.CharField(
        max_length=TABLE_NAME_MAX_LENGTH,
        validators=(
            validate_only_letters_and_spaces,
        )
    )

    table_sizes = models.CharField(
        max_length=TABLE_SIZES_MAX_LENGTH
    )

    table_price = models.IntegerField()



