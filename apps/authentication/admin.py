from django.contrib import admin
from apps.authentication.models import User, Address, Unregistered_User, User_Address
import nested_admin


# class AddressInline(nested_admin.NestedStackedInline):
#     fields = ['address', 'city', 'postal_code', 'country']
#     model = Address


# class UserInline(nested_admin.NestedStackedInline):
#     model = User


# class User_AddressInline(nested_admin.NestedTabularInline):
#     model = User_Address
#     inlines = [AddressInline, UserInline]


@admin.register(User)
class AuthorAdmin(nested_admin.NestedModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_used_address')
    # inlines = [
    #     User_AddressInline,
    # ]


@admin.register(Unregistered_User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    list_displays = ('address', 'city', 'country', 'postal_code')
