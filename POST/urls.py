from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('details/<int:pk>', PostDetailView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
