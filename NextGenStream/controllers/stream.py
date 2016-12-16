from django.http import HttpResponse
from django.shortcuts import render

def get_stream(req):
    return render(req, 'NextGenStream/home.html')
