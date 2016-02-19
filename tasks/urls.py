from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'remove', views.say_whatsup, name='remove'),
    url(r'complete', views.say_whatsup, name='complete'),
    url(r'create', views.say_whatsup, name='create'),
]

