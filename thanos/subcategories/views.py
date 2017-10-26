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
from .models import SubCategory
from .serializers import (
    SubCategoryCreateSerializer,
    SubCategoryListSerializer,
    SubCategoryDetailSerializer,
    SubCategorySerializer,
    )

class SubCategoryCreateAPIView(CreateAPIView):
    queryset = SubCategory.objects.select_related().all()
    serializer_class = SubCategoryCreateSerializer

class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.select_related().all()
    serializer_class = SubCategoryListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class SubCategoryDetailAPIView(RetrieveAPIView):
    queryset = SubCategory.objects.select_related().filter(id__gte=0)
    serializer_class = SubCategoryDetailSerializer

class SubCategoryUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SubCategory.objects.select_related().all()
    serializer_class = SubCategorySerializer