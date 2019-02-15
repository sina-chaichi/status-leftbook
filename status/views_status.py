from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from status import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)

# Create your views here.


class PostDetailView(DetailView):
    model = models.Post


class PostCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'status/post_detail.html'
    form_class = forms.PostForm
    model = models.Post


class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'status/post_detail.html'
    form_class = forms.PostForm
    model = models.Post

class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = models.Post
    success_url = reverse_lazy('post_list')



@login_required
def post_publish(request,pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)
