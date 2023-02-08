from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import ContentForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, "posts.html", {'posts': posts})


def delete(request, post_ID):
    post = Post.objects.get(id=post_ID)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_ID):
    post = Post.objects.get(id=post_ID)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "edit.html", {"post": post})


def LikePost(request, post_ID):
    post = Post.objects.get(id=post_ID)
    new_value = post.likes+1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
