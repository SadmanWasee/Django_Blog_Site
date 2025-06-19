from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
# Create your views here.

class IndexView(View):
    
    def get(self,request):
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "index.html", {
            "posts":latest_posts
        })
    
class AllPostsView(View):

    def get(self,request):
        all_posts = Post.objects.all().order_by("-date")
        return render(request, "all_posts.html",{
            "posts": all_posts
        })

class UploadPostView(View):

    def get(self,request):
        form = PostForm()

        return render(request, "upload_post.html", {
            "form":form
        })
    def post(self, request):
        form = PostForm(request.POST, request.FILES)  # Include request.FILES if you're uploading files
        if form.is_valid():
            form.save()
            return redirect("index-page")  # Ensure "index" is defined in urls.py
        return render(request, "upload_post.html", {
            "form": form  # Re-render form with errors
        })
