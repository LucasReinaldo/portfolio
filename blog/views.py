from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog


def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs': blogs})


@login_required(login_url="/accounts/signup")
def createpost(request):
    if request.method == 'POST':
        newpost = Blog()
        newpost.title = request.POST['title']
        newpost.body = request.POST['body']
        newpost.pub_date = timezone.datetime.now()
        newpost.writer = request.user
        newpost.image = request.FILES['fileInput']
        newpost.save()
        return redirect('/blog/post/' + str(newpost.id))
    else:
        return render(request, 'blog/createpost.html')


def post(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/post.html', {'post': post})


def upvote(request, blog_id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, pk=blog_id)
        post.votes += 1
        post.save()
        return redirect('/blog/post/' + str(post.id))
