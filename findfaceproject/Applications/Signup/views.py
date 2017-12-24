from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
def get_name(request):
    # if this is a POST request we need to process the form data
    subscribers = Subscriber.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriberForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #return HttpResponseRedirect("http://127.0.0.1:8000/home/")
            form.save()
            print(Subscriber.objects.all())
            email = Subscriber.email
            name = form.cleaned_data['username']
            print(name)

    else:
        form = Subscriber()

    return render(request, 'signup.html', locals())
