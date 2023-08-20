from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Comment, CommentUserLike


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'updated_on')


class CommentLikes_Inline(admin.TabularInline):
    model = CommentUserLike
    extra = 0


@admin.register(Comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_author_full_name', 'user', 'content', 'get_post')
    inlines = [
        CommentLikes_Inline,
    ]

    @admin.display(description='Post')
    def get_post(self, obj):
        return ", ".join([
            obj.post.title
        ])


