from django.urls import path
from .views import home, create_entry, register, dashboard, settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'journal/login.html'), name ='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('new/', create_entry, name='create_entry'),
    path('register/', register, name='register'),
    path('settings/', settings, name='settings'),
]