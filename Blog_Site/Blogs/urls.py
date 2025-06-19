from django.urls import path
from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("all-posts/", views.AllPostsView.as_view(), name = "all-posts-page"),
    path("upload-post/", views.UploadPostView.as_view(), name = "upload-post-page"),
    path("all-posts/<str:slug>", views.PostDetailView.as_view(), name="post-detail-page")
]
