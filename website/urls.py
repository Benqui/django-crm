
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_usr, name='login'),
    path('logout/', views.logout_usr, name='logout'),
    path('register/', views.register_usr, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
]

#no mames esto lo esto haciendo en neovim

