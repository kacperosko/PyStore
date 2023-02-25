from django.contrib import admin
from apps.authentication.models import User


@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'staff')
