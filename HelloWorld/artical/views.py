from django.shortcuts import render
from django.http import HttpResponse
from artical.models import Artical
# Create your views here.

def home(request):
        return HttpResponse("Hello World, Django")

def detail(request, my_args):
    post = Artical.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, data_time = %s, content=%s" %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)