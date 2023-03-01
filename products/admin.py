from django.contrib import admin
from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('short_description',)
    search_fields = ('name',)

