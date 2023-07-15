from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from catalog.views import UserPasswordResetView
from users.apps import UsersConfig
from .views import UserPasswordResetView

from users.views import RegisterView, UserUpdateView

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('reset/', UserPasswordResetView.as_view(), name='password_reset'),

]
