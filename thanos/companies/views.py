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
from .models import Company
from .serializers import (
    CompanyCreateSerializer,
    CompanyListSerializer,
    CompanyDetailSerializer,
    CompanySerializer,
    )

class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.select_related().all()
    serializer_class = CompanyCreateSerializer

class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.select_related().all()
    serializer_class = CompanyListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class CompanyDetailAPIView(RetrieveAPIView):
    queryset = Company.objects.select_related().filter(id__gte=0)
    serializer_class = CompanyDetailSerializer

class CompanyUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Company.objects.select_related().all()
    serializer_class = CompanySerializer