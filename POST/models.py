from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Medium(models.Model):
    type = models.CharField(max_length=255, default='Untitled')

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    image = CloudinaryField('image', default='placeholder')
    header_image = CloudinaryField('header_image', default='placeholder')
    title = models.CharField(max_length=255, default='Untitled')
    title_tag = models.CharField(max_length=255,)
    description = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post_date = models.DateField(auto_now_add=True)
    medium = models.CharField(max_length=255, default='uncategorised')


def __str__(self):
    return self.description + '|' + str(self.author)


def get_absolute_url(self):
    return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
