from django.contrib.auth import logout

from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, PostImage

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'rental/blog.html', {'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'rental/detail.html', {
        'post':post,
        'photos':photos,
    })
    
def notice(request):
    return render(request,'notice/noticeboard.html')

def store(request):
    return render(request,'store/store.html')

def home(request):
    return render(request,'home/home.html')

def logout(request):
     logout(request)
     return redirect('logout')