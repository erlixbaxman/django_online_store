from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    readonly_fields = ('short_description',)
    search_fields = ('name',)
