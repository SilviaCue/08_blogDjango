from django.urls import path
from blogApp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
path('contacto', views.contacto, name="Contacto"),    

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
