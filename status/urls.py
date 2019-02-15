from django.urls import path, re_path
from website.views import views_home
from status import views_status, views_comment, views_like

urlpatterns =[
    path('', views_home.PostListView.as_view() , name='post_list'),
    path('about/', views_home.AboutView.as_view() , name='about'),
    re_path('post/(?P<pk>\d+)$',views_status.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views_status.PostCreateView.as_view(), name='post_new'),
    re_path('post/(?P<pk>\d+)/edit/$',views_status.PostUpdateView.as_view(), name='post_edit'),
    re_path('post/(?P<pk>\d+)/remove/$',views_status.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views_home.DraftListView.as_view(), name='draft_list'),
    re_path('post/(?P<pk>\d+)/comment/$',views_comment.add_comment, name='add_comment'),
    re_path('comment/(?P<pk>\d+)/approve/$',views_comment.comment_approval, name='comment_approval'),
    re_path('comment/(?P<pk>\d+)/remove/$',views_comment.comment_remove, name='comment_remove'),
    re_path('post/(?P<pk>\d+)/like/$', views_like.like_button_clicked, name='do_like'),
    re_path('post/(?P<pk>\d+)/publish/$',views_status.post_publish, name='post_publish'),


]
