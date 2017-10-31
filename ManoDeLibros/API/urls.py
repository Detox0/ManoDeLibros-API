from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^dealers/todos$', views.dealer_list),
    url(r'^dealers/ciudad/(?P<ciudad>[\w\-]+)$', views.dealer_city),
    url(r'^dealers/region/(?P<pk>[0-9]+)$', views.dealer_region),
    url(r'^dealers/catalogo$', views.add_libro_catalogo),
    url(r'^dealers/catalogo/(?P<pk>[0-9]+)$', views.dealer_catalogo),
    url(r'^libros/todos$', views.libros_list),
    url(r'^libros/crear$', views.create_libro),
    url(r'^regiones/$', views.region_list),
    url(r'^generos/todos$', views.genero_list),
    url(r'^direcciones/$', views.direccion_list),
    url(r'^autores/todos$', views.autor_list),
    url(r'^autores/crear$', views.create_autor),
]
