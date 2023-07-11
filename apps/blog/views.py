from django.shortcuts import render
from .models import Post, Comment


def get_all_posts(request):
    posts = Post.objects.filter(status=1)

    content = {"posts": posts}

    return render(request, 'blog/blog-home.html', content)


def get_post(request, article_slug):
    post = Post.objects.get(slug=article_slug)
    comments = Comment.objects.filter(post=post)
    content = {"post": post, "comments": comments}

    return render(request, 'blog/blog-post.html', content)
