from django.shortcuts import render

def detail_pojistence(request):
    return render(request, "pojisteni/detail_pojistence.html", dict(jmeno="Rozárka Nejkrásnější", adresa="Praha", pojisteni="žádné"))