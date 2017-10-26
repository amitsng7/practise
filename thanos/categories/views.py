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
from .models import Category
from .serializers import (
    CategoryCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategorySerializer,
    )

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.select_related().all()
    serializer_class = CategoryCreateSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.select_related().all()
    serializer_class = CategoryListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.select_related().filter(id__gte=0)
    serializer_class = CategoryDetailSerializer

class CategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer