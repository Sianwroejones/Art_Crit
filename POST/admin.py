from django.contrib import admin
from .models import Post, Medium, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Medium)
admin.site.register(Comment)
