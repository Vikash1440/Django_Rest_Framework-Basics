from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student(requst):
    studnts_data=[
        {'id':1,'name':'syaml'}
    ]
    return HttpResponse(studnts_data)