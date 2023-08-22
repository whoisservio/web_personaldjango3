from django.shortcuts import render, HttpResponse

html_base ="""
    <h1>Mi primera pagina web</h1>
  
"""

# Create your views here.
def home (request):
    return render(request,"core/home.html")

def about(request):
   return render(request, "core/about.html")

def contact(request): 
    return render(request, "core/contact.html")