from django.http import HttpResponse
from django.shortcuts import render 

def edit(request):
    return render(request,'edit.html')

def graph(request):
    return render(request,'graph.html')


def co(request):
    return render(request,'co.html')