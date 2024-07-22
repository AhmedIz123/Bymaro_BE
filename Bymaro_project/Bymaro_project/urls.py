from django.contrib import admin
from django.urls import path,include
from Authentification import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('Authentification.urls')),
    path('api/admin/', include('admin_custom.urls')),
]