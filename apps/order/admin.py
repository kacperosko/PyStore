from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Discount, Order, Order_Item, Payment_Type, Payment


@admin.register(Discount)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')


class Order_ItemInline(admin.TabularInline):
    model = Order_Item
    extra = 0
    readonly_fields = ['price', 'quantity', 'product']


@admin.register(Order)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'user' ,'unregistered_user' , 'amount', 'payment')
    inlines = [
        Order_ItemInline,
    ]
    list_filter = ['user']


@admin.register(Order_Item)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'order', 'quantity', 'price')

    @admin.display(description="Product")
    def get_product_name(self, obj):
        return obj.product.name


@admin.register(Payment_Type)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('payment_name',)


@admin.register(Payment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'deadline', 'is_paid')