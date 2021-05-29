from django.urls import path
from .views import (BlogDetailView,
                    BlogListView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView, 
                    UserBlogListView)
from . import views
urlpatterns = [
    path('', BlogListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserBlogListView.as_view(), name="user-posts"),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about"),
]
