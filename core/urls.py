from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cervezas/$', views.cervezas, name='cervezas'),
    url(r'^contacto/', views.ContactFormView.as_view(), name='contacto'),
]
