from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import BlogPost


def get_date(post):
    return post.date

def landing_page(request):
    sorted_posts = sorted(BlogPost.objects.all(), key=get_date)
    return render(request, "blog/index.html", {
        "posts": sorted_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": BlogPost.objects.all(),
    })

def single_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": post,
        "title": post.title,
        "author": post.author,
        "content": post.content,
    })