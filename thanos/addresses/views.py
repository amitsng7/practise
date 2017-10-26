from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
    )
# from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )
from .models import Address
from .serializers import (
    AddressCreateSerializer,
    AddressListSerializer,
    AddressDetailSerializer,
    AddressSerializer,
    )

class AddressCreateAPIView(CreateAPIView):
    queryset = Address.objects.select_related().all()
    serializer_class = AddressCreateSerializer

class AddressListAPIView(ListAPIView):
    queryset = Address.objects.select_related().all()
    serializer_class = AddressListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class AddressDetailAPIView(RetrieveAPIView):
    queryset = Address.objects.select_related().filter(id__gte=0)
    serializer_class = AddressDetailSerializer

class AddressUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Address.objects.select_related().all()
    serializer_class = AddressSerializer