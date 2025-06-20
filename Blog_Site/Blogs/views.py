from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import  UpdateView, DeleteView
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

class PostDetailView(View):

    def get(self,request,slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request,"post-detail-page.html", {
            "post":post
        })
    
class PostDeleteView(DeleteView):

    model = Post
    template_name = 'delete_post.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('index-page')

class PostUpdateView(UpdateView):

    model = Post 
    form_class = PostForm
    template_name = 'update-post.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('index-page')
