from django.shortcuts import render
from django.utils import timezone
from status import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView)

# Create your views here.


class AboutView(TemplateView):
    template_name = 'home/about.html'

class PostListView(ListView):
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')

class DraftListView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'status/post_list.html'
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.filter(posted_at__isnull=True).order_by('-created_at')
