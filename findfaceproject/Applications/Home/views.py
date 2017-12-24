from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def ResponseForHome(request):

   hello = "Hello"
   current_day = timezone.now()
   return render(request, "index.html", locals())

