from django.shortcuts import render
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