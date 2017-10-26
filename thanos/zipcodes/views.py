from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
    )
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    )
from .models import Zipcode
from .serializers import (
    ZipcodeCreateSerializer,
    ZipcodeListSerializer,
    ZipcodeDetailSerializer,
    )

class ZipcodeCreateAPIView(CreateAPIView):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeCreateSerializer

class ZipcodeListAPIView(ListAPIView):
    queryset = Zipcode.objects.all()
    serializer_class = ZipcodeListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['Zipcode', 'state']

class ZipcodeDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
	queryset = Zipcode.objects.filter(zipcode__gte=0)
	serializer_class = ZipcodeDetailSerializer

	def put(self, instance, *args, **kwargs):
		return self.update(instance, *args, **kwargs)
	def delete(self, instance, *args, **kwargs):
		return self.destroy(instance, *args, **kwargs)