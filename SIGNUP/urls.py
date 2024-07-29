from django.urls import path
from.views import UserRegistrationView, CustomLogoutView
from django.contrib.auth import logout

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]
