from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^dealers/todos$', views.dealer_list),
    url(r'^dealers/ciudad/(?P<ciudad>[\w\-]+)$', views.dealer_city),
    url(r'^dealers/region/(?P<pk>[0-9]+)$', views.dealer_region),
    url(r'^dealers/catalogo$', views.add_libro_catalogo),
    url(r'^dealers/(?P<pk>[0-9]+)/catalogo$', views.dealer_catalogo),
    url(r'^dealers/catalogo/todos$', views.all_dealer_catalogos),
    url(r'^libros/todos$', views.libros_list),
    url(r'^libros/genero/(?P<pk>[0-9]+)$', views.libros_genero),
    url(r'^libros/crear$', views.create_libro),
    url(r'^libros/ultimos/(?P<cantidad>[0-9]+)$', views.ultimos_libros),
    url(r'^regiones/todas$', views.region_list),

    url(r'^generar_pago/subject=(?P<data_subject>[a-zA-Z0-9 ]+)&amount=(?P<data_amount>[\w\-]+)&payer_email=(?P<data_payer_email>[^@]+@[^@]+\.[^@]+)&pedido_id=(?P<pedido_id>[a-zA-Z0-9 ]+)&notify_url=(?P<data_notify_url>http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)&return_url=(?P<data_return_url>http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)&cancel_url=(?P<data_cancel_url>http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)$', views.generar_pago),

    url(r'^libros$', views.libros_avanzado.as_view()),
    url(r'^dealers$', views.dealer_avanzado.as_view()),
    url(r'^pedidos$', views.pedido_avanzado.as_view()),
    url(r'^pedidos/libros$', views.pedido_Libro_avanzado.as_view()),
    url(r'^dealer/catalogo$', views.catalogo_avanzado.as_view()),
    url(r'^lector$', views.lector_avanzado.as_view()),


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

    url(r'^editoriales/todas$', views.all_editoriales),

    url(r'^lectores/crear$', views.create_lector),
    url(r'^lectores/pedidos', views.add_lector_pedido),
]
