from django.db import models
from apps.authentication.models import User
from django.utils.text import slugify
from apps.models_handler.generate_file_directory import generate_post_path
from ckeditor.fields import RichTextField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    content = RichTextField()
    post_image = models.FileField(upload_to=generate_post_path, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    content = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user', blank=True, null=True)
    author_first_name = models.CharField(max_length=100, blank=True, null=True)
    author_last_name = models.CharField(max_length=100, blank=True, null=True)
    likes = None
    liked_by_current_user = False
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def get_author_full_name(self):
        return self.author_first_name + " " + self.author_last_name

    def save(self, *args, **kwargs):
        if self.user is not None:
            self.author = self.user.get_full_name()
        super(Comment, self).save(*args, **kwargs)


class CommentUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentuserlike_user', blank=True,
                             null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='commentuserlike_comment',
                                blank=True, null=True)
    isliked = models.BooleanField(default=True)
