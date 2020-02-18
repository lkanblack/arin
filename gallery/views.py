from django.shortcuts import render
from .models import Post

# Create your views here.
def gallery_list(request):
    posts = Post.objects.all()
    return render(request, 'gallery/gallery_list.html', {'posts': posts})