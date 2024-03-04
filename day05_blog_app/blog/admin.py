from django.contrib import admin
from .models import BlogPost, Author

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    list_display = ("title", "author", "content")

    list_filter = ("title", "author", )


admin.site.register(BlogPost, MovieAdmin)
admin.site.register(Author)