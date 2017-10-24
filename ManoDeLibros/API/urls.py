from django.conf.urls import url
from API import views

urlpatterns = [
    url(r'^dealers/$', views.dealer_list),
]
