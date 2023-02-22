from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, Attribute, Product_Attribute


class ProductInline(admin.TabularInline):
    model = Product_Attribute

@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_created')
    inlines = [
        ProductInline,
    ]


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Attribute)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)\


@admin.register(Product_Attribute)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id_product', 'id_attribute')

