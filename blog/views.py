from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.utils import timezone

from django.core.paginator import Paginator

from .models import Blog
from .forms import PostForm


def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 9)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request, 'blog/blog_list.html', {'blogs': blogs})


def detail(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': post})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create_post = form.save(commit=False)
            create_post.writer = request.user
            create_post.pub_date = timezone.now()
            create_post.save()
            return redirect('/blog/detail/' + str(create_post.id))
    else:
        form = PostForm()
    return render(request, 'blog/blog_form.html', {'form': form})


@login_required(login_url="/accounts/signup")
def update(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        update_post = form.save(commit=False)
        update_post.pub_date = timezone.now()
        update_post.save()
        return redirect('/blog/detail/' + str(post.id))
    return render(request, 'blog/blog_form.html', {'form': form})


@login_required(login_url="/accounts/signup")
def delete(request, blog_id):
    delete_post = Blog.objects.get(pk=blog_id)
    delete_post.delete()
    return redirect('/blog/')


def upvote(request, blog_id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, pk=blog_id)
        post.votes += 1
        post.save()
        return redirect('/blog/detail/' + str(post.id))
