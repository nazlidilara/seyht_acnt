from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text="merhaba django"
    return HttpResponse("You're looking at question %s" % text)