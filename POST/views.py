from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Medium
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ["-post_date"]

class PostDetailView(DetailView):
    model = Post 
    template_name = 'post_details.html'  

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'description',)

class AddMediumView(CreateView):
        model = Medium
        #form_class = PostForm
        template_name = 'add_medium.html'
        fields = '__all__'
        #fields = ('title', 'description',)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'description', 'medium',]

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def MediumView(request, meds):
    medium_posts = Post.objects.filter(medium=meds.replace('-', ' '))
    return render(request, 'medium.html', {'meds':meds, 'medium_posts':medium_posts})