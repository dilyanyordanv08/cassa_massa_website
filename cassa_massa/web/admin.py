from django.contrib import admin

from cassa_massa.web.models import Contact


@admin.register(Contact)
class Contacts(admin.ModelAdmin):
    pass

