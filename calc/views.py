from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'Kritika'})

def add(request):
    v1 = int(request.POST['n1'])
    v2 = int(request.POST['n2'])
    res = v1 + v2
    return render(request,"home.html",{"result": res,'name':'Kritika'})
