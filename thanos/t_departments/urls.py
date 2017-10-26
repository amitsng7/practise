from django.conf.urls import url
from .views import (
	DepartmentCreateAPIView,
	DepartmentUpdateAPIView,
	DepartmentListAPIView,
	DepartmentDetailAPIView,
	)

urlpatterns = [
	url(r'^$', DepartmentListAPIView.as_view(), name='list'),
    url(r'^create/$', DepartmentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', DepartmentDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', DepartmentUpdateAPIView.as_view(), name='update'),
]
