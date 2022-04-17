from django.contrib import admin

from cassa_massa.web.models import Contact, Services


@admin.register(Contact)
class Contacts(admin.ModelAdmin):
    pass


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
