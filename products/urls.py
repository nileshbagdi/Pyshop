from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = (
    path('', views.index, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
)

