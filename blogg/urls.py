from django.urls import path
from blogg import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
