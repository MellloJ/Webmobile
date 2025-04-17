from django.contrib import admin
from django.urls import include, path

from core.views import Login, Logout

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
