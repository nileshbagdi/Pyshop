from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = (
    path('', views.index, name='home'),
    path('new/', views.new),
    path('dp/', views.dp),
    path('signup/', views.register, name='Sign Up'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
)

