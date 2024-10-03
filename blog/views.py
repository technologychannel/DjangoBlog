from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request,"blog/index.html",{'allposts': posts})

def single_page(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/single_post.html', {'post': post})