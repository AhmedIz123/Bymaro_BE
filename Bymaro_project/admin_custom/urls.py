from django.urls import re_path,path

from . import views

urlpatterns = [
    path('create_user/', views.admin_create_user),
    path('update_user/<int:id>/', views.admin_update_user),
    path('delete_user/<int:id>/', views.admin_delete_user),
    path('users/',views.users_list),
]