from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth import logout


# Create your views here.

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully. Please log in."

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


class CustomLogoutView(SuccessMessageMixin, RedirectView):
    url = reverse_lazy('login')
    success_message = "You have been successfully logged out."

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(self.request, self.success_message)
        return super().get(request, *args, **kwargs)
