from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from .models import Blog
from .forms import PostForm


def blog(request):
    blogs = Blog.objects.all().order_by('-pub_date')
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
            messages.success(request, 'Your post has been created!')
            return HttpResponseRedirect(create_post.get_absolute_url())
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
        messages.success(request, 'Your post has been updated!')
        return HttpResponseRedirect(post.get_absolute_url())
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


def search_query(request):
    if request.method == "GET":
        search = Blog.objects.all().order_by('-pub_date')
        q = request.GET.get('q', '')

        if q is not None:
            search = search.filter(
                Q(title__icontains=q) | Q(body__icontains=q)).distinct()

        return render(request, 'blog/blog_list.html', {'blogs': search})
