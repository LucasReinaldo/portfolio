from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog
from .forms import PostForm


def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': post})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.title = request.POST['title']
            new_post.body = request.POST['body']
            new_post.image = request.FILES['fileInput']
            new_post.pub_date = timezone.datetime.now()
            new_post.author = request.user
            new_post.save()
            return redirect('/detail/' + str(new_post.id))
    else:
        form = PostForm()
        return render(request, 'blog/blog_detail.html', {'form': form})


def update(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('/detail/' + str(blog.id))
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/blog_form.html', {'form': form})


def delete(request, blog_id):
    post = Blog.objects.get(pk=blog_id)
    post.delete()
    return redirect('/blog/')


def upvote(request, blog_id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, pk=blog_id)
        post.votes += 1
        post.save()
        return redirect('/blog/detail/' + str(post.id))
