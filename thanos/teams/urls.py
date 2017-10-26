from django.conf.urls import url
from .views import (
	TeamCreateAPIView,
	TeamUpdateAPIView,
	TeamListAPIView,
	TeamDetailAPIView,
	)

urlpatterns = [
	url(r'^$', TeamListAPIView.as_view(), name='list'),
    url(r'^create/$', TeamCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TeamDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', TeamUpdateAPIView.as_view(), name='update'),
]
