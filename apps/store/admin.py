from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, Attribute, Product_Attribute
from django.utils.html import format_html


class ProductInline(admin.TabularInline):
    model = Product_Attribute
    extra = 0


@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    @admin.display(description="Image preview")
    def image_tag(self, obj):
        return format_html('<img style="height: 100px" src="{}" />'.format(obj.image.url))

    list_display = ('name', 'price', 'category', 'is_active', 'image_tag', 'date_created')
    list_filter = ['is_active']
    readonly_fields = ('image_tag',)
    inlines = [
        ProductInline,
    ]


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Attribute)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product_Attribute)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id_product', 'id_attribute')

