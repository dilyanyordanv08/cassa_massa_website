from django.contrib import admin

from cassa_massa.web.models import Contact, Services, FinishedProducts, Category, Images


@admin.register(Contact)
class Contacts(admin.ModelAdmin):
    pass


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ('service_order', 'name', 'description', 'image')


@admin.register(FinishedProducts)
class FinishedProducts(admin.ModelAdmin):
    list_display = ('table_name', 'table_sizes', 'table_price')
    search_fields = ('table_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    search_fields = ('title',)

