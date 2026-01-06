from django.shortcuts import render, HttpResponse

# Create your views here.
def index(ctx):
    return HttpResponse("<h1>Hello, Mom!</h1>")
