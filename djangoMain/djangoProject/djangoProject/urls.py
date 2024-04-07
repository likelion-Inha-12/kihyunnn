from django.contrib import admin
from django.urls import path

from util import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', views.health),
]