from django.urls import path
from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page"),
    path("all-posts/", views.AllPostsView.as_view(), name = "all-posts-page"),
    path("all-posts/<str:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
    path("all-posts/<str:slug>/delete", views.PostDeleteView.as_view(), name="post-delete-page"),
    path("all-posts/<str:slug>/update",views.PostUpdateView.as_view(), name="post-update-page"),
    path("upload-post/", views.UploadPostView.as_view(), name = "upload-post-page"),
   
]
