from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^serviceapi/$', views.serviceapi,name="serviceapi"),
    url(r'^$', views.index, name="home"),
]