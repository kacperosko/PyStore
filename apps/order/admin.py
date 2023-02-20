from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Discount

@admin.register(Discount)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

