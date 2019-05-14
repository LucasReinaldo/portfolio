from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog


def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs': blogs})


def post(request, blog_id):
    postblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/post.html', {'blog':postblog})


@login_required
def createpost(request):
    if request.method == 'POST':
        createpost = Blog()
        createpost.title = request.POST['title']
        createpost.body = request.POST['body']
        createpost.pub_date = timezone.datetime.now()
        createpost.writer = request.user
        createpost.image = request.FILES['fileInput']
        createpost.save()
        return redirect('blog')
    else:
        return render(request, 'blog/createpost.html')
