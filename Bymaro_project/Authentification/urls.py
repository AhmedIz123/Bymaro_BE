from django.urls import re_path,path

from . import views

urlpatterns = [
    path('login', views.login),
    path('test_token', views.test_token),
    path('logout',views.logout),
]