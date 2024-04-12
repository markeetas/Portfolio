from django.urls import path
from . import views

urlpatterns = [
    path("", views.detail_pojistence, name="pojisteni_detail_pojistence"),
]