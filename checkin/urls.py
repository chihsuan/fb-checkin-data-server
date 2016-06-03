from django.conf.urls import url
from checkin import views

urlpatterns = [
    url(r'^create/$', views.create, name='checkin.create'),
    url(r'^place/$', views.create_place, name='checkin.place'),
    url(r'^read/$', views.read, name='checkin.read')
]
