from django.conf.urls import url
from .views import (
	SubCategoryCreateAPIView,
	SubCategoryUpdateAPIView,
	SubCategoryListAPIView,
	SubCategoryDetailAPIView,
	)

urlpatterns = [
	url(r'^$', SubCategoryListAPIView.as_view(), name='list'),
    url(r'^create/$', SubCategoryCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', SubCategoryDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', SubCategoryUpdateAPIView.as_view(), name='update'),
]
