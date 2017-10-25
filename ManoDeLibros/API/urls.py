from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^dealers/$', views.dealer_list),
    url(r'^libros/$', views.libros_list),
    url(r'^regiones/$', views.region_list),
    url(r'^generos/$', views.genero_list),
]
