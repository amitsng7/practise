from django.conf.urls import url		
from .views import (
	ZipcodeCreateAPIView,
	ZipcodeListAPIView, 
	ZipcodeDetailAPIView,
	)	

urlpatterns = [
	url(r'^$', ZipcodeListAPIView.as_view(), name='list'),
    url(r'^create/$', ZipcodeCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ZipcodeDetailAPIView.as_view(), name='detail'),
]
