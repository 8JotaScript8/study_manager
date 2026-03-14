from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import HomeView
from tasks.views import signupview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    path('signup/', signupview, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('tasks/', include('tasks.urls')),
    path('subjects/', include('subjects.urls')),
]