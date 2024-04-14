from django.urls import path
from . import views

urlpatterns = [
    path("insured_index/", views.InsuredIndex.as_view(), name="insured_index"),
    path("<int:pk>/insured_detail/", views.CurrentInsured.as_view(), name="insured_detail"),
]