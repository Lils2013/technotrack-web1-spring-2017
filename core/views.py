from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse('test passed, {}'.format(request.GET['a']))