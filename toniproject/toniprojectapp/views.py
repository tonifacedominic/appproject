

from  django.http import HttpResponse
from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
       obj=place.objects.all()
       tdata =teaminfo.objects.all()
       return render(request,"index.html", {'result':obj,'tdata':tdata})

       # tdata=teaminfo.objects.all()
       # return render(request, "index.html",{'tdata':tdata})


# def about(request):
#     return render(request,"aboutold.html")
#
# def contact(request):
#     return render(request,"contactlistold.html")

# def addition(request):
#     return render(request, "addition.html")
#
# def result(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET ['num2'])
#     result = x + y
#     return render(request, 'result.html', {'res': result})
