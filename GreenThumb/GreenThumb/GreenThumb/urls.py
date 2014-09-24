from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]