from django.contrib import admin
from apps.authentication.models import User, Address, Unregistered_User, User_Address
# import nested_admin


# class AddressInline(nested_admin.NestedStackedInline):
#     fields = ['address', 'city', 'postal_code', 'country']
#     model = Address


# class UserInline(nested_admin.NestedStackedInline):
#     model = User


# class User_AddressInline(nested_admin.NestedTabularInline):
#     model = User_Address
#     inlines = [AddressInline, UserInline]

admin.site.site_header = "PyStore"


# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'get_last_address',)

    @admin.display(ordering='last_used_address', description='Address')
    def get_last_address(self, obj):
        return f"{obj.last_used_address.address}, {obj.last_used_address.city} {obj.last_used_address.postal_code}"


admin.site.register(User, UserAdmin)


@admin.register(Unregistered_User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'address')


@admin.register(Address)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'country', 'postal_code', 'user_display', 'unregistered_user_display')

    @admin.display(description='User')
    def user_display(self, obj):
        return ", ".join([
            user.get_full_name() for user in User.objects.filter(addresses=obj)
        ])

    @admin.display(description='Uregistered User')
    def unregistered_user_display(self, obj):
        return ", ".join([
            user.get_full_name() for user in Unregistered_User.objects.filter(address=obj)
        ])



# @admin.register(User_Address)
class User_AddressAdmin(admin.ModelAdmin):
    model = User_Address
    list_display = ('name', 'get_user', 'get_address', )

    @admin.display(ordering='user', description='User')
    def get_user(self, obj):
        print(obj.user.first_name)
        return obj.user.get_full_name()

    @admin.display(ordering='address', description='Address')
    def get_address(self, obj):
        print(obj.address.address)
        return obj.address

    # def children_display(self, obj):
    #     return ", ".join([
    #         address.city for address in obj.address.all()
    #     ])

    # children_display.short_description = "Address"


admin.site.register(User_Address, User_AddressAdmin)
