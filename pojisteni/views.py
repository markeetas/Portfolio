from django.shortcuts import render
from django.views import generic
from .models import Insurance, Insured, InsuranceEvent, UserRole, Statistics


class InsuredIndex(generic.ListView):

    template_name = "pojisteni/insured_index.html"  
    context_object_name = "insureds"  

    def get_queryset(self):
        return Insured.objects.all()
    
class CurrentInsured(generic.DetailView):

    model = Insured
    template_name = "pojisteni/insured_detail.html"    