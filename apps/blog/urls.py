# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.blog import views


urlpatterns = [
    path('blog', views.get_all_posts, name='blog_posts'),
    path('blog/<article_slug>', views.PostComment.as_view(), name='blog_post'),
    path('ajax/likecomment', views.like_comment, name='blog_likecomment'),

]
