from django import forms
from .models import Post, Medium

#choices = [('Painting', 'Painting'), ('Print', 'Print'), ('Drawing', 'Drawing'),
#('Ceramics', 'Ceramics'), ('Mixed Media', 'Mixed Media'), ('Sculpture', 'Sculpture'), 
#('Wood', 'Wood'), ('Collage', 'Collage'), ('Photography', 'Photography'), ('Other', 'Other'),]
choices = Medium.objects.all().values_list('type', 'type')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'medium', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder':'user name'}),
            'medium': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type title of artwork here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'medium': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }       