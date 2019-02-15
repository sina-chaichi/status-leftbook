from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from status import models, forms
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def add_comment(request,pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request, 'status/comment_form.html', {'form':form})


@login_required
def comment_approval(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(models.Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
    
