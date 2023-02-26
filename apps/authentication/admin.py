from django.contrib import admin
from apps.authentication.models import User, Address


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'staff')


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    list_displays = ('address', 'city', 'country', 'postal_code')