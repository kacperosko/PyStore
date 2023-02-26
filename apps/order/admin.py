from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Discount, Order, Order_Item, Payment_Type, Payment


@admin.register(Discount)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')


@admin.register(Order)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'user', 'payment')


@admin.register(Order_Item)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('order', 'selected_attributes', 'quantity', 'price')


@admin.register(Payment_Type)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('payment_name',)


@admin.register(Payment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'deadline', 'is_paid')