from django.contrib import admin

from cassa_massa.web.models import Contact, Services, FinishedProducts


@admin.register(Contact)
class Contacts(admin.ModelAdmin):
    pass


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


@admin.register(FinishedProducts)
class FinishedProducts(admin.ModelAdmin):
    list_display = ('table_name', 'table_sizes', 'table_price')
