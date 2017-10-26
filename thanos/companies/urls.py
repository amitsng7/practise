from django.conf.urls import url
from .views import (
	CompanyCreateAPIView,
	CompanyUpdateAPIView,
	CompanyListAPIView,
	CompanyDetailAPIView,
	)

urlpatterns = [
	url(r'^$', CompanyListAPIView.as_view(), name='list'),
    url(r'^create/$', CompanyCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CompanyDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', CompanyUpdateAPIView.as_view(), name='update'),
]
