from django.shortcuts import render
from django.views import generic
from .models import Insurance, Insured, InsuranceEvent, UserRole, Statistics
from .forms import InsuredForm
from django.views.generic.base import TemplateView


class InsuredIndex(generic.ListView):

    template_name = "pojisteni/insured_index.html"  
    context_object_name = "insureds"  

    def get_queryset(self):
        return Insured.objects.all()
    
    
class InsuranceIndex(generic.ListView):
    template_name = "pojisteni/insurance_index.html"
    context_object_name = "insurances"

    def get_queryset(self):
        return Insurance.objects.all()    
    
class CurrentInsured(generic.DetailView):

    model = Insured
    template_name = "pojisteni/insured_detail.html"    
    
class CreateInsured(generic.edit.CreateView):
    form_class = InsuredForm  
    template_name = "pojisteni/create_insured.html"

   
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        
        return render(request, self.template_name, {"form": form})  
    
class About(generic.TemplateView):
    template_name = "pojisteni/about.html"    
    
class EventsIndex(generic.ListView):  # přidáno
    template_name = "pojisteni/events_index.html"
    context_object_name = "events"

    def get_queryset(self):
        return InsuranceEvent.objects.all()    
    
class HomeView(TemplateView):
    template_name = 'pojisteni/home.html'    