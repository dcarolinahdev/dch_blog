from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(), active=True).order_by('-published_date')

class DraftView(generic.ListView):
    template_name = 'blog/drafts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
