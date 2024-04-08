from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class GreetingView(View):
  greetingMessage = '<b>Creating Class Based Views</b>'
  def get(self,request):
    return HttpResponse(self.greetingMessage)