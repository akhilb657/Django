from django.shortcuts import render

# Create your views here.
def electronics(request):
  product_dict={
    'product1':'Iphone',
    'product2':'Mac',
    'product3':'Dell'
  }
  return render(request,'productApp/products.html',product_dict)

def toys(request):
  product_dict={
    'product1':'teddy',
    'product2':'train',
    'product3':'car'
  }
  return render(request,'productApp/products.html',product_dict)

def shoes(request):
  product_dict={
    'product1':'nike',
    'product2':'puma',
    'product3':'adidas'
  }
  return render(request,'productApp/products.html',product_dict)

def index(request):
  return render(request,'productApp/index.html')