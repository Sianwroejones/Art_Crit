from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
   image = models.ImageField()
   title = models.CharField(max_length=255, default='Untitled')
   title_tag = models.CharField(max_length=255, default='Untitled')
   description = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.description + '|' + str(self.author)

#class Comment(models.Model):
#   post = models.ForeignKey(Post, on_delete=models.CASCADE)
#    text = models.TextField()
#    author = models.ForeignKey(User, on_delete=models.CASCADE)
#    created = models.DateTimeField(auto_now_add=True)    
#    modified = models.DateTimeField(auto_now=True)
