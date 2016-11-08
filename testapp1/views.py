from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<p>Hello! This is testapp1 speaking!</p>')
