from django.contrib import admin
from inventory.models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
