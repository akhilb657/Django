from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):
  return HttpResponse("Do your best. Work daily! It's You vs You")
