from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeView(request,*args, **kwargs):
    context = {
        "username":request.user,
        "numList":[12,3585,15,83,122,53,846]
    }
    return render(request, "home.html", context)

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")