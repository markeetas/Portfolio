from django.urls import path
from . import views, url_handlers

urlpatterns = [
    path("insured_index/", views.InsuredIndex.as_view(), name="insured_index"),
    path("<int:pk>/insured_detail/", views.CurrentInsured.as_view(), name="insured_detail"),
    path("create_insured/", views.CreateInsured.as_view(), name="novy_pojisteny"),
    path("insurance_index/", views.InsuranceIndex.as_view(), name="insurance_index"),
    path("about/", views.About.as_view(), name="about"),
    path("events_index/", views.EventsIndex.as_view(), name="events_index"),
    path('', views.HomeView.as_view(), name='home'),
    path("", url_handlers.index_handler),
]

