from django.contrib import (admin)
from .models import Product, Category


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(Product, ShopAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)



