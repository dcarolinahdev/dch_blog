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

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    """def get_queryset(self):
        #Excludes any posts that aren't published yet.
        return Post.objects.filter(published_date__lte=timezone.now())"""

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'action': 'Edit', 'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('blog:post_draft_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'action': 'New', 'form': form})
