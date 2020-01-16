from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Plano


def index(request):
    return HttpResponse('Hello, welcome to the index page.')

def plano(request):
    return HttpResponse('Os planos vao aqui...')

def individual_post(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content) 
