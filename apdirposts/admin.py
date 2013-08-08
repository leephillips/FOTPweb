from models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
   fields = ['author', 'title', 'pub_date', 'content']

admin.site.register(Post, PostAdmin)
