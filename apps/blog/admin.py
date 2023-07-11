from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'updated_on')
