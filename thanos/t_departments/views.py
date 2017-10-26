from django.shortcuts import render

# Create your views here.
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
from .models import t_Department
from .serializers import (
    DepartmentCreateSerializer,
    DepartmentListSerializer,
    DepartmentDetailSerializer,
    DepartmentSerializer,
    )

class DepartmentCreateAPIView(CreateAPIView):
    queryset = t_Department.objects.select_related().all()
    serializer_class = DepartmentCreateSerializer

class DepartmentListAPIView(ListAPIView):
    queryset = t_Department.objects.select_related().all()
    serializer_class = DepartmentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class DepartmentDetailAPIView(RetrieveAPIView):
    queryset = t_Department.objects.select_related().filter(id__gte=0)
    serializer_class = DepartmentDetailSerializer

class DepartmentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = t_Department.objects.select_related().all()
    serializer_class = DepartmentSerializer