from django.shortcuts import render

# Create your views here.

def ResponseForAbout(request):
   return render(request, "about.html")