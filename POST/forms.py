from django import forms
from .models import Post, Medium, Comment

choices = Medium.objects.all().values_list('type', 'type')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'author', 'medium',
            'description', 'header_image'
            )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'user',
                    'type': 'hidden'
                }
            ),
            'medium': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'description')

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Type title of artwork here'
                }
            ),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
