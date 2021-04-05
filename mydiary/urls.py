"""mydiary urls linked myproject urls.py"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new/", views.new, name="new"),
    path("detail/<int:index>", views.detail, name="detail"),
    path("edit/<int:index>", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
