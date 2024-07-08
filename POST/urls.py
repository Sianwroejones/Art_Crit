from django.urls import path
# from . import views
from .views import HomeView, PostDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('details/<int:pk>', PostDetailView.as_view(), name='details'),
]
