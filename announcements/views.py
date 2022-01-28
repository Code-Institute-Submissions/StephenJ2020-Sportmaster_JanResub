""" import post model to add/edit and display posts"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm
from .forms import PostForm


def announcements(request):
    """ BLog page displaying all posts """

    posts = Post.objects.all()
    post_count = len(posts)
    template = 'announcements/announcements.html'
    context = {
        'posts': posts,
        'post_count': post_count
    }
    return render(request, template, context)


def post_detail(request, slug):
    """ Display each Post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    template = 'announcements/post_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """ Add a post to the announcements """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only our staff have access to post \
            New Product Announcements.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'New product announcement successfully \
                added!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Post failed, please check if form is valid.')
    else:
        form = PostForm()

    template = 'announcements/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):
    """ Edit an existing Post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only our staff have access to edit \
            Product Announcements.')
        return redirect(reverse('homepage'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated  Announcement!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(
                request, 'Update failed, please check if form is valid')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'announcements/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only our staff have access to delete \
            Product Announcements.')
        return redirect(reverse('homepage'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'post deleted!')
    return redirect(reverse('post_detail'))
