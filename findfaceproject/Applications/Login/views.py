from django.http import HttpResponseRedirect
from django.shortcuts import render
from findfaceproject.Applications.Signup.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import *
# Create your views here.
response = " "
def SignInResponse(request):
    # if this is a POST request we need to process the form data
    obj = Subscriber.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriberForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['username']
            for i in obj:
                if form.cleaned_data['email'] == i.email and form.cleaned_data['password'] == i.password:
                    response = "Authoresation done succesfully"
                    request.session['user'] = True
                    user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
                    #return HttpResponseRedirect("http://127.0.0.1:8000/search/")
                else:
                    request.session['user'] = False
                    response = "Sorry, but you are not registered yet"
                    #return HttpResponseRedirect("http://127.0.0.1:8000/search/")
    else:
        form = Subscriber()

    return render(request, 'logIn.html', locals())