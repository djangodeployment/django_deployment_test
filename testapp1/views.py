from django.shortcuts import render


def index(request):
    return render(request, 'testapp1/index.html')
