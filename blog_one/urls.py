from django.urls import path
from blog_one import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('drafts/', views.DraftListView.as_view(), name='draft_list'),
    path('post/<int:pk>/comment/', views.addCommentPost, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.commentApproved, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.commentRemove, name='comment_remove'),
    path('post/<int:pk>/publish/', views.postPublish, name='post_publish'),
]