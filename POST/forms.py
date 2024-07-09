from django import forms
from .models import Post

choices = [('Painting', 'Painting'), ('Print', 'Print'), ('Drawing', 'Drawing'),
 ('Ceramics', 'Ceramics'), ('Mixed Media', 'Mixed Media'), ('Sculpture', 'Sculpture'), 
 ('Wood', 'Wood'), ('Collage', 'Collage'), ('Photography', 'Photography'), ('Other', 'Other'),]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'medium', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type title of artwork here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'medium': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type title of artwork here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }       