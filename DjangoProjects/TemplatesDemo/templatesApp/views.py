from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
  myDict = {"name":"Akhil"}
  return render(request,'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request):
  myDict = {"id":111,"name":"Ranga","salary":10000}
  return render(request,'templatesApp/employeeTemplate.html',myDict)