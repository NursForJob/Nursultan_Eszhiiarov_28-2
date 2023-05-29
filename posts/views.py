import datetime

from django.shortcuts import HttpResponse, render
from posts.models import Post
# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == "GET":
        current_date = datetime.datetime.now()
        return HttpResponse(f'Date: {current_date}')


def good_bye(request):
    if request.method == "GET":
        return HttpResponse('Goodby user!')


def main_page_view(request):
    if request.method == 'GET':
         return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, id_):
    if request.method == "GET":
        post = Post.objects.get(id=id_)
        context = {
            'post': post,
            'comments': post.comment_set.all()
        }
        return render(request, 'posts/detail.html', context=context)
