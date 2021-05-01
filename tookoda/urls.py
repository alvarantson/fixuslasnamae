from django.urls import path, re_path
from . import views

urlpatterns = [
    path("/hooldus", views.hooldus),
    path("/rehvivahetus", views.rehvivahetus)

]