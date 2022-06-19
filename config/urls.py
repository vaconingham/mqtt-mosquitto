from django.contrib import admin
from django.urls import path, include
from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
]
