from django.shortcuts import render
from django.http import HttpResponse
from artical.models import Artical
from datetime import datetime
# Create your views here.

def home(request):
        post_list = Artical.objects.all()
        return render(request, 'hello.html', {'post_list': post_list})

def detail(request, my_args):
    post = Artical.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, data_time = %s, content=%s" %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def test(request) :
        return render(request, 'test.html', {'current_time': datetime.now()})