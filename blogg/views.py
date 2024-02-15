from django.shortcuts import render
from blogg.models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, "blogg/home.html", {"posts": posts})
