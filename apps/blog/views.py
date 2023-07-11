from django.shortcuts import render
from .models import Post


def get_all_articles(request):
    print("BLOG")
    posts = Post.objects.filter(status=1)

    content = {"posts": posts}

    return render(request, 'blog/blog-home.html', content)