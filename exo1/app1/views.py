from django.shortcuts import render

# Create your views here.

def index(r):
    ctx={}
    return render(r,"app1/index.html",ctx)