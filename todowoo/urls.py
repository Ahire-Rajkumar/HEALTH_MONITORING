"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth URLs
    path('signup/', views.signupuser, name='signupuser'),
    path('doctor_signupuser/', views.doctor_signupuser, name='doctor_signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Django's built-in authentication URLs (includes password reset)
    # This line provides URLs like /accounts/password_reset/, /accounts/reset/<uidb64>/<token>/, etc.
    path('accounts/', include('django.contrib.auth.urls')),


    path('check_detail/', views.check_detail, name='check_detail'),


    # Todo/Health-related URLs
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
    path('predict/', views.predict_disease, name='predict_disease'),
    path('predict/predicted_result/', views.predicted_results, name='predicted_result'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('your_profile/', views.your_profile, name='your_profile'),

]