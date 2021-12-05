from django.contrib import admin
from .models import Product, Category


# In the tuple below changing the list order below will change the order 
# in which they are displayed on the site
class ProductAdmin(admin.ModelAdmin):
    """ Product Admin Class """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    # To reverse the order put a - infront of sku


class CategoryAdmin(admin.ModelAdmin):
    """ Category Admin Class """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
