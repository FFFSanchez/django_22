from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def bibus(requests):
    return f'abobus'

def index(request):
    return HttpResponse('<p>Hi Mir</p>')