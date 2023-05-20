from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('<marquee><h1>srujana tinnavara, Era vadilestunnavara.....</h1></marquee')

def revi(request):
    return HttpResponse('<marquee><b>mama kutti, long drive podama.....</b></marquee>')