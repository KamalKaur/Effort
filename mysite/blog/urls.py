#::::::::::::::IMPORT THE HEADER FILE HERE::::::::::::::::::::::::::::::#
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::#

#:::::::::::::::DEFINE THE URLS HERE::::::::::::::::::::::::::::::::::::#

urlpatterns = patterns('',
   url(r'^$', views.index, name='index')
   url(r'^$', views    
    
)
