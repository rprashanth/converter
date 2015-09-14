from django.conf.urls import patterns, include, url
from pr3 import views

urlpatterns = patterns('',
    url(r'^$',views.start),
    url(r'^convert/$' ,views.convert),
    url(r'^convert1/$' ,views.convert1),   
)
