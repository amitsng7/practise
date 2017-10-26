from django.conf.urls import url
from .views import (
	CategoryCreateAPIView,
	CategoryUpdateAPIView,
	CategoryListAPIView,
	CategoryDetailAPIView,
	)

urlpatterns = [
	url(r'^$', CategoryListAPIView.as_view(), name='list'),
    url(r'^create/$', CategoryCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CategoryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', CategoryUpdateAPIView.as_view(), name='update'),
]
