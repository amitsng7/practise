from django.conf.urls import url
from .views import (
	GroupCreateAPIView,
	GroupUpdateAPIView,
	GroupListAPIView,
	GroupDetailAPIView,
	)

urlpatterns = [
	url(r'^$', GroupListAPIView.as_view(), name='list'),
    url(r'^create/$', GroupCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', GroupDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', GroupUpdateAPIView.as_view(), name='update'),
]
