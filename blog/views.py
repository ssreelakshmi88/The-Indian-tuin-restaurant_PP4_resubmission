from django.shortcuts import render, get_object_or_404, reverse
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.db.models import Count
from django.contrib import messages


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'page_obj': page_obj,
    }
    return render(
        request, 'posts/post_list.html', context)


def post_detail(request, slug):
    post_detail = Post.objects.all()
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)
    
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(
                    request, 'Comment awaiting approval.'
                    )
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'liked': liked,
        "comment_form": CommentForm(),
        'commented': True,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(
        request, 'posts/post_detail.html', context)


def post_like(request, slug, *args, **kwargs):
    post = Post.objects.get(id=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


