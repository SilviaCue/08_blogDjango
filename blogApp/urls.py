from django.urls import path
from blogApp import views




urlpatterns = [
    path('contacto', views.contacto, name="Contacto"),

]
