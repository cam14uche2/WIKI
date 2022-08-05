from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('uche', views.search, name="search"),
]