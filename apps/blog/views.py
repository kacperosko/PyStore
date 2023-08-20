from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Post, Comment, CommentUserLike
from .forms import CommentForm
from django.views.generic import View
from django.db.models import Count
from ..order.views import is_ajax


def like_comment(request):
    context = {}
    if is_ajax(request) and request.method == "GET":
        if not request.user.is_authenticated:
            context['message'] = 'You must log in to like a comment'
            return JsonResponse(context, status=401)
        comment_id = request.GET.get("comment_id", None)
        isliked = True if request.GET.get("isliked", None) == "true" else False
        try:
            liked, created = CommentUserLike.objects.update_or_create(user=request.user, comment_id=comment_id, defaults={"isliked": isliked})
            context['counter'] = CommentUserLike.objects.filter(comment_id=comment_id, isliked=True).count()
        except Exception as e:
            print("ERROR", e)
            context["message"] = "Error"
            return JsonResponse(context, status=401)
        return JsonResponse(context, status=200)
    return JsonResponse(context, status=400)


def get_all_posts(request):
    posts = Post.objects.filter(status=1)

    content = {"posts": posts}

    return render(request, 'blog/blog-home.html', content)


class PostComment(View):

    @staticmethod
    def get(request, article_slug):
        post = Post.objects.get(slug=article_slug)
        comments = Comment.objects.filter(post=post)
        for c in comments:
            c.likes = CommentUserLike.objects.filter(comment=c, isliked=True).count()
            if request.user.is_authenticated:
                c.liked_by_current_user = CommentUserLike.objects.filter(user=request.user, comment=c, isliked=True).exists()
        content = {}
        content["post"] = post
        content["comments"] = comments
        content["form"] = CommentForm()

        return render(request, 'blog/blog-post.html', content)

    @staticmethod
    def post(request, article_slug):
        form = CommentForm(request.POST)
        if request.method == "POST" and request.user.is_authenticated:
            updated_data = request.POST.copy()
            updated_data.update({
                'first_name': request.user.first_name,
                'last_name': request.user.last_name
            })
            form = CommentForm(data=updated_data)

        if request.method == "POST" and form.is_valid():

            comment = Comment(content=form.cleaned_data["content"],
                              author_first_name=form.cleaned_data["first_name"], author_last_name=form.cleaned_data["last_name"],
                              post=Post.objects.get(slug=article_slug), user=request.user if request.user.is_authenticated else None)
            comment.save()
            return redirect(f"/blog/{article_slug}#comment-{comment.id}")
        else:
            return PostComment.get(request, article_slug)
