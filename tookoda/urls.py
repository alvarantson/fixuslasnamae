from django.urls import path, re_path
from . import views

urlpatterns = [
    path("tookoda/hooldus/", views.hooldus),
    path("tookoda/rehvivahetus/", views.rehvivahetus)

]