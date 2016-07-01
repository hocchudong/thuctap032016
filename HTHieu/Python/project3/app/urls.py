from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^HomePage/$', views.login, name='login'),
    url(r'^HomePage/getatrr/$', views.getatrr, name='atrr'),
    url(r'^HomePage/execute/$', views.execute, name='execute'),
    url(r'^HomePage/getpath/$', views.getpath, name='path'),
    url(r'^HomePage/getfile/$', views.getfile, name='file'),
    url(r'^HomePage/changefile/$', views.changefile, name='change'),
    url(r'^HomePage/shortfile/$', views.shortfile, name='short'),
]
