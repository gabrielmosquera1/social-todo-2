from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'register', views.register, name='register'),
    url(r'login', views.login_view, name='login'),
    url(r'logout', views.logout_view, name='logout'),
]

