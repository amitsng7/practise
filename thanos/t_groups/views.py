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
from .models import t_Group
from .serializers import (
    GroupCreateSerializer,
    GroupListSerializer,
    GroupDetailSerializer,
    GroupSerializer,
    )

class GroupCreateAPIView(CreateAPIView):
    queryset = t_Group.objects.select_related().all()
    serializer_class = GroupCreateSerializer

class GroupListAPIView(ListAPIView):
    queryset = t_Group.objects.select_related().all()
    serializer_class = GroupListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class GroupDetailAPIView(RetrieveAPIView):
    queryset = t_Group.objects.select_related().filter(id__gte=0)
    serializer_class = GroupDetailSerializer

class GroupUpdateAPIView(RetrieveUpdateAPIView):
    queryset = t_Group.objects.select_related().all()
    serializer_class = GroupSerializer