from django.contrib import admin
from django.urls import path

from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plans/', plans),
    path('', loginView),
    path('logout/', logOutView),
    path('register/', register),
    path('delete/<int:num>/', delete),


]
