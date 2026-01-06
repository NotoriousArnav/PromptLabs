from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Prompt
from .serializers import PromptSerializer

# REST API Views
class PromptViewSet(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
   
# Create your views here.
def index(ctx):
    return HttpResponse("<h1>Hello, Mom!</h1>")
