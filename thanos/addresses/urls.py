from django.conf.urls import url		
from .views import (
	AddressCreateAPIView,
	AddressListAPIView, 
	AddressDetailAPIView,
	AddressUpdateAPIView,
	)	

urlpatterns = [
	url(r'^$', AddressListAPIView.as_view(), name='list'),
    url(r'^create/$', AddressCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', AddressDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', AddressUpdateAPIView.as_view(), name='update'),
]
