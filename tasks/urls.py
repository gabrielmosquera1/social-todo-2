from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'remove', views.remove, name='remove'),
    url(r'complete', views.complete, name='complete'),
    url(r'create', views.create, name='create'),
]

