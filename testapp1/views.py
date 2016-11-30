from django.core.cache import cache
from django.shortcuts import render


def index(request):
    # Dummy caching commands to verify that cache is working
    c = cache.get('my_key')
    if c is None:
        cache.set('my_key', 'cached')
        c = 'None'
    return render(request, 'testapp1/index.html', context={ 'c': c })
