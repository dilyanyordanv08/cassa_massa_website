from django.contrib import admin

from cassa_massa.web.models import Contact, Services, FinishedProducts, Category, Images, Post, PhotoAlbum, Reviews

from django import forms


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


#
# @admin.register(Images)
# class ImagesAdmin(admin.ModelAdmin):
#     list_filter = ('category',)
#     search_fields = ('title',)


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'body',)


class ImagesForm(forms.ModelForm):
    model = Images

    class Media:
        js = (
            '/static/js/jquery-latest.js',
            '/static/js/ui.base.js',
            '/static/js/ui.sortable.js',
            '/static/js/menu-sort.js',
        )


class PhotoAlbumInline(admin.StackedInline):
    model = PhotoAlbum


admin.site.register(
    Images,
    inlines=[PhotoAlbumInline],
    form=ImagesForm,
    list_filter=('category',),
    search_fields=('title',)
)

"""
/* menu-sort.js */

jQuery(function($) {
    $('div.inline-group').sortable({
        /*containment: 'parent',
        zindex: 10, */
        items: 'div.inline-related',
        handle: 'h3:first',
        update: function() {
            $(this).find('div.inline-related').each(function(i) {
                if ($(this).find('input[id$=name]').val()) {
                    $(this).find('input[id$=order]').val(i+1);
                }
            });
        }
    });
    $('div.inline-related h3').css('cursor', 'move');
    $('div.inline-related').find('input[id$=order]').parent('div').hide();
});
"""


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'description',)