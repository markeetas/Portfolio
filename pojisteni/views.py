from django.shortcuts import render
from django.views import generic
from .models import Insurance, Insured, InsuranceEvent, UserRole, Statistics
from .forms import InsuredForm


class InsuredIndex(generic.ListView):

    template_name = "pojisteni/insured_index.html"  
    context_object_name = "insureds"  

    def get_queryset(self):
        return Insured.objects.all()
    
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