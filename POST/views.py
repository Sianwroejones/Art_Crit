from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Medium, Comment 
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ["-post_date"]
    meds = Medium.objects.all()

    def get_context_data(self, *args, **kwargs):
        meds_menu = Medium.objects.all()   
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["meds_menu"] = meds_menu
        return context

class PostDetailView(DetailView):
    model = Post 
    template_name = 'post_details.html'  

    def get_context_data(self, *args, **kwargs):
        meds_menu = Medium.objects.all()   
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["meds_menu"] = meds_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'description',)

    def get_context_data(self, *args, **kwargs):
        meds_menu = Medium.objects.all()   
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["meds_menu"] = meds_menu
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #fields = ('title', 'description',)

    def get_context_data(self, *args, **kwargs):
        meds_menu = Medium.objects.all()   
        context = super(AddCommentView, self).get_context_data(*args, **kwargs)
        context["meds_menu"] = meds_menu
        return context

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AddMediumView(CreateView):
        model = Medium
        #form_class = PostForm
        template_name = 'add_medium.html'
        fields = '__all__'
        #fields = ('title', 'description',)

        def get_context_data(self, *args, **kwargs):
            meds_menu = Medium.objects.all()   
            context = super(AddMediumView, self).get_context_data(*args, **kwargs)
            context["meds_menu"] = meds_menu
            return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'description', 'medium',]

def get_context_data(self, *args, **kwargs):
            meds_menu = Medium.objects.all()   
            context = super(UpdatepostView, self).get_context_data(*args, **kwargs)
            context["meds_menu"] = meds_menu
            return context
        

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def get_context_data(self, *args, **kwargs):
            meds_menu = Medium.objects.all()   
            context = super(DeletePostView, self).get_context_data(*args, **kwargs)
            context["meds_menu"] = meds_menu
            return context

def MediumView(request, meds):
    medium_posts = Post.objects.filter(medium=meds.replace('-', ' '))
    return render(request, 'medium.html', {'meds':meds.title(), 'medium_posts':medium_posts})

