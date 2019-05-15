from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog
from .forms import PostForm


class BlogList(ListView):
    model = Blog


class BlogDetail(DetailView):
    model = Blog


class BlogCreate(CreateView):
    model = Blog
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog_post')


class BlogUpdate(UpdateView):
    model = Blog
    fields = ('title', 'body', 'image')
    success_url = reverse_lazy('blog_post')


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_post')


@login_required(login_url="/accounts/signup")
def createpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/blog_edit.html', {'form': form})


def upvote(request, blog_id):
    if request.method == 'POST':
        post = get_object_or_404(Blog, pk=blog_id)
        post.votes += 1
        post.save()
        return redirect('/blog/detail/' + str(post.id))
