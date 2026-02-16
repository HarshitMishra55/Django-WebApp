from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    return HttpResponse("Hello Django")


def test(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())


def show(request):
    template = loader.get_template("show.html")
    return HttpResponse(template.render())
