from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from status import models, forms
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def already_liked_post(user, post_id):

    post= Post.objects.get(id=post_id)
    return Like.objects.filter(user=user, post=post).exists()

@login_required
def like_button_clicked(request, post_id):
    post = Post.objects.get(id=post_id)

    if not already_liked_post(request.user, post_id):
        Like.objects.create(user=request.user, post=post, timestamp=datetime.now())
    else:
        Like.objects.filter(user=request.user, post=post).delete()

    return redirect(reverse('post_list'))
