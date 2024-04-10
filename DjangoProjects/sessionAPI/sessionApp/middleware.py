from django.http import HttpResponse

class MiddleWareLifeCycle:
  def __init__(self,get_response):
    print("init method")
    self.get_response = get_response
  
  def __call__(self,request):
    print("Before view is executed")
    response = self.get_response(request)
    print("After view is executed")
    return response

class ExceptionHandlingMiddleWare:
  def __init__(self,get_response):
    self.get_response = get_response
  
  def __call__(self,request):
    response = self.get_response(request)
    return response
  
  def process_exception(self,request,exception):
    print(exception.__class__.__name__)
    print(exception)
    return HttpResponse("<b>Currently we are under maintainance</b>")