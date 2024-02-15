from django.shortcuts import render, HttpResponse

# Create your views here.




def contacto(request):
    return render(request, "blogApp/contacto.html")
