from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^dealers/todos$', views.dealer_list),
    url(r'^dealers/ciudad/(?P<ciudad>[\w\-]+)$', views.dealer_city),
    url(r'^dealers/region/(?P<pk>[0-9]+)$', views.dealer_region),
    url(r'^dealers/catalogo$', views.add_libro_catalogo),
    url(r'^dealers/catalogo/(?P<pk>[0-9]+)$', views.dealer_catalogo),
    url(r'^dealers/catalogo/todos$', views.all_dealer_catalogos),
    url(r'^libros/todos$', views.libros_list),
    url(r'^libros/genero/(?P<pk>[0-9]+)$', views.libros_genero),
    url(r'^libros/crear$', views.create_libro),
    url(r'^regiones/todas$', views.region_list),


    url(r'^libros$', views.libros_avanzado.as_view()),
    url(r'^dealers$', views.dealer_avanzado.as_view()),
    url(r'^pedidos$', views.pedido_avanzado.as_view()),
    url(r'^pedidos/libros$', views.pedido_Libro_avanzado.as_view()),
    url(r'^dealer/catalogo$', views.catalogo_avanzado.as_view()),


    url(r'^ciudades/region/(?P<pk>[0-9]+)$', views.ciudades_region),
    url(r'^generos/todos$', views.genero_list),
    url(r'^direcciones/$', views.direccion_list),
    url(r'^autores/todos$', views.autor_list),
    url(r'^autores/crear$', views.create_autor),

    url(r'^pedidos/todos$', views.all_pedidos),
    url(r'^pedidos/crear$', views.create_pedido),
    url(r'^pedidos/agregar/libro', views.add_libro_pedido),
    url(r'^pedidos/libros/(?P<pk>[0-9]+)$', views.libros_pedido),

    url(r'^usuarios/todos$', views.all_users),

]
