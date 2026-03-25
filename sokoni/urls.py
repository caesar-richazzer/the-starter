# buzztier/urls.py (Main project URLs)
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Import auth views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home_view, name='home'),
    path('register/', user_views.register_view, name='register'),
    
    # Login/Logout built-in paths
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]