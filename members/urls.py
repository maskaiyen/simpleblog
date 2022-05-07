from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordChangingView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('login/', UserSignInView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/',PasswordChangingView.as_view()), # () 裡可以pass 'template_name', 'success_url', can make this to views.
    path('password_success/', views.password_success, name='password_success'),
]