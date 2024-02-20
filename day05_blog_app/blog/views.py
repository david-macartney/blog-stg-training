from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "smoothie-recipe",
        "image": "smoothie1.jpg",
        "author": "David",
        "date": date(2024, 2, 20),
        "summary": "Start your day by waking up",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam aliquam, 
            laboriosam saepe pariatur, excepturi quidem quisquam nam rerum eligendi animi 
            maxime vel tempore neque! Ut ipsam blanditiis in quisquam fugit.
        """
    },
    {
        "slug": "glass-recipe",
        "image": "eyeglass.jpg",
        "author": "David",
        "date": date(2024, 1, 20),
        "summary": "Take a look through the eyeglass",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam aliquam, 
            laboriosam saepe pariatur, excepturi quidem quisquam nam rerum eligendi animi 
            maxime vel tempore neque! Ut ipsam blanditiis in quisquam fugit.
        """
    },
    {
        "slug": "penguin-recipe",
        "image": "random.jpg",
        "author": "David",
        "date": date(2024, 1, 15),
        "summary": "Use AI to generate fun images",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam aliquam, 
            laboriosam saepe pariatur, excepturi quidem quisquam nam rerum eligendi animi 
            maxime vel tempore neque! Ut ipsam blanditiis in quisquam fugit.
        """
    },
]

def get_date(post):
    return post["date"]

def landing_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })

def single_post(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
    })
