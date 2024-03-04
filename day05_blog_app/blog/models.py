from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="blog_posts")
    content = models.TextField(null=True)
    date = models.DateField(null=True)
    image = models.ImageField(upload_to="static/blog/images", null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self) -> str:
        return f"(Title: {self.title}, Author: {self.author})"