from django.shortcuts import render
from blogg.models import Post, Categoria

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, "blogg/home.html", {"posts": posts})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blogg/categoria.html", {"categoria": categoria, "posts": posts})


"""def categoria(request, categoria_id):
    print("Recibiendo solicitud para la categoría con ID:", categoria_id)
    categoria = Categoria.objects.get(id=categoria_id)
    print("Categoría encontrada:", categoria)
    posts = Post.objects.filter(categorias=categoria)
    print("Posts asociados:", posts)
    return render(request, "blogg/categoria.html", {"categoria": categoria, "posts": posts})"""
