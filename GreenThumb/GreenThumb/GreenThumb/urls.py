from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'dht', views.DHTSensorsViewSet)

urlpatterns = [
    url(r'^api/sensors/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]