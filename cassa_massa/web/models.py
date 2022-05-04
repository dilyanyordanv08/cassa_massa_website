from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

from cassa_massa.settings import AUTH_USER_MODEL
from cassa_massa.web.validators import validate_only_letters_and_spaces


AppUser = get_user_model()


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

    service_order = models.IntegerField()

    name = models.CharField(
        max_length=SERVICES_NAME_MAX_LENGTH,
        validators=(
            validate_only_letters_and_spaces,
        )
    )

    image = models.ImageField()

    description = models.TextField(
    )

    class Meta:
        ordering = ['service_order', 'description']

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


class TableContactForm(models.Model):
    NAME_MAX_LENGTH = 25
    CELL_PHONE_MAX_LENGTH = 10
    CELL_PHONE_MIN_LENGTH = 10
    EMAIL_MESSAGE_MAX_LENGTH = 500

    DINING_TABLE = "Трапезна маса"
    COFFEE_TABLE = "Кафе маса"
    CORNER_TABLE = "Крайна маса"

    ROUND_SHAPE = "Кръгла"
    SQUARE_SHAPE = "Квадратна"
    RECTANGULAR_SHAPE = "Правоъгълна"

    RIVER_TABLE = "River"
    DOUBLE_RIVER = "Double River"
    EPOXY_EDGE = "Epoxy Edge"

    EUROPEAN_WALNUT = "Европейски Орех"
    AMERICAN_WALNUT = "Американски Орех"
    ELM = "Бряст"
    OAK = "Дъб"
    CHERRY_WOOD = "Череша"
    OLIVE = "Маслина"
    OTHER_EXOTIC_WOOD = "Друга екзотична дървесина"

    BRIGHT_BLUE = "Светльо синьо"
    WHITE_PEARL = "Бяла перла"
    GREEN = "Зелено"
    GOLD = "Златно"
    DARK_BLUE = "Тъмно синьо"
    SOLID_BLACK = "Плътно черно"
    RED = "Червено"
    GRAY = "Сиво"
    PURPLE = "Лилаво"
    COLORLESS = "Безцветна"

    METAL_LEGS = "Метални крака"
    WOOD_LEGS = "Дървени крака"

    MATTE_OIL = "Масло мат"
    SATIN_OIL = "Масло сатен"
    GLOSS_OIL = "Масло гланц"

    TYPES_OF_TABLES = [(x, x) for x in (DINING_TABLE, COFFEE_TABLE, CORNER_TABLE)]

    table_type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES_OF_TABLES),
        choices=TYPES_OF_TABLES,
    )

    number_of_seats = models.IntegerField()

    TABLE_TOP_SHAPE = [(x, x) for x in (ROUND_SHAPE, SQUARE_SHAPE, RECTANGULAR_SHAPE)]

    table_shape = models.CharField(
        max_length=max(len(x) for (x, _) in TABLE_TOP_SHAPE),
        choices=TABLE_TOP_SHAPE,
    )

    ARRANGEMENT = [(x, x) for x in (RIVER_TABLE, DOUBLE_RIVER, EPOXY_EDGE)]

    table_arrangement = models.CharField(
        max_length=max(len(x) for (x, _) in ARRANGEMENT),
        choices=ARRANGEMENT,
    )

    TYPE_OF_WOOD = [(x, x) for x in (EUROPEAN_WALNUT, AMERICAN_WALNUT, OAK, CHERRY_WOOD,
                                     OLIVE, OTHER_EXOTIC_WOOD)]

    wood_type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPE_OF_WOOD),
        choices=TYPE_OF_WOOD
    )

    EPOXY_COLOR = [(x, x) for x in (BRIGHT_BLUE, WHITE_PEARL, GREEN, GOLD, DARK_BLUE, SOLID_BLACK,
                                    RED, GRAY, PURPLE, COLORLESS)]

    table_epoxy_color = models.CharField(
        max_length=max(len(x) for (x, _) in EPOXY_COLOR),
        choices=EPOXY_COLOR,
    )

    METAL_LEGS_TYPES = [(x, x) for x in (METAL_LEGS, WOOD_LEGS)]

    table_legs = models.CharField(
        max_length=max(len(x) for (x, _) in METAL_LEGS_TYPES),
        choices=METAL_LEGS_TYPES
    )

    TOP_OIL = [(x, x) for x in (SATIN_OIL, GLOSS_OIL, MATTE_OIL)]

    table_top_oil = models.CharField(
        max_length=max(len(x) for (x, _) in TOP_OIL),
        choices=TOP_OIL,
    )

    customer_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validate_only_letters_and_spaces,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    cell_phone_number = models.CharField(
        max_length=CELL_PHONE_MAX_LENGTH,
        validators=(
            MinLengthValidator(CELL_PHONE_MIN_LENGTH),
        )
    )

    message = models.TextField(
        max_length=EMAIL_MESSAGE_MAX_LENGTH,
    )

    def __str__(self):
        return self.email


class Category(models.Model):
    category_title = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.category_title


class Images(models.Model):
    title = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    category_image = models.ImageField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    slug = models.SlugField(
        null=True,
    )

    def get_absolute_url(self):
        return reverse("table-details", kwargs={"slug": self.slug})


class PhotoAlbum(models.Model):
    menu = models.ForeignKey(
        Images,
        on_delete=models.CASCADE,
        related_name="child_images",
        )

    image = models.ImageField()

    order = models.IntegerField(
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.menu

    class Meta:
        ordering = ('order',)


class Post(models.Model):
    title = models.CharField(
        max_length=200,
    )

    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )

    body = models.TextField()

    image = models.ImageField()

    slug = models.SlugField(
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})


class Reviews(models.Model):
    NAME_MAX_LENGTH = 25

    author = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    description = models.TextField()

    def __str__(self):
        return self.author


# class Person(models.Model):
#     VAT_MIN_LENGTH = 10
#     Customer_first_name = models.CharField(
#         max_length=30,
#         null=True,
#         blank=True,
#     )
#     Customer_family_name = models.CharField(
#         max_length=30,
#         null=True,
#         blank=True,
#     )
#     Customer_address = models.CharField(max_length=60)
#     Customer_order = models.TextField()
#     Customer_order_price = models.IntegerField()
#     Customer_satisfaction_score = models.IntegerField()
#     Company_name = models.CharField(
#         max_length=30,
#         null=True,
#         blank=True,
#     )
#     Company_vat_number = models.CharField(
#         max_length=10,
#         validators=(
#             MinLengthValidator(VAT_MIN_LENGTH)
#         ),
#         null=True,
#         blank=True,
#     )
#     customer_telephone_number = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.Customer_first_name
