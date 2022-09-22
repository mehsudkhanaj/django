import http
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    mydict={'insert_me':"Now i am comming from first_app/index.htm"}
    
    return render(request, 'first_app/index.html',context=mydict)