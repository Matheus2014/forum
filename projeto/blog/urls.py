from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^tutoriais/(?P<cat>\w+)/$', views.menu),
    url(r'^duvidas/(?P<cat>\w+)/$', views.duvida),
    url(r'^post/(?P<id>[0-9]+)/$', views.detalhe),
]