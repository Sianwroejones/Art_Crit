from django.urls import path
from .views import SplashPageView

urlpatterns = [
    path('', SplashPageView.as_view(), name='splashpage'),
]