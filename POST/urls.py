from django.urls import path
# from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddMediumView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('details/<int:pk>', PostDetailView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_medium/', AddMediumView.as_view(), name='add_medium'),
    path('details/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'), 
    path('details/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'), 
]
