from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    # return HttpResponse("Hello, world. You're at the app index")
    # template = loader.get_template('app/index.html')
    # return HttpResponse(template)
    return render(request, 'app/index.html')
# Create your views here.
