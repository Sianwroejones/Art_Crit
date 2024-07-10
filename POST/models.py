from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Medium(models.Model):
    type = models.CharField(max_length=255, default='Untitled')

    def __str__(self):
       return self.type 

    def get_absolute_url(self): 
       #return reverse('details', args=(str(self.id)))  
       return reverse('home') 

class Post(models.Model):
   image = models.ImageField()
   title = models.CharField(max_length=255, default='Untitled')
   title_tag = models.CharField(max_length=255,)
   description = RichTextField(blank=True, null=True)
   #description = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)
   post_date = models.DateField(auto_now_add=True)
   medium = models.CharField(max_length=255, default='uncategorised')

   def __str__(self):
       return self.description + '|' + str(self.author)

   def get_absolute_url(self): 
       #return reverse('details', args=(str(self.id)))  
       return reverse('home') 



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)    
    modified = models.DateTimeField(auto_now=True)
