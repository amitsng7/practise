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
from .models import Team
from .serializers import (
    TeamCreateSerializer,
    TeamListSerializer,
    TeamDetailSerializer,
    TeamSerializer,
    )

class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.select_related().all()
    serializer_class = TeamCreateSerializer

class TeamListAPIView(ListAPIView):
    queryset = Team.objects.select_related().all()
    serializer_class = TeamListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['zipcode']

class TeamDetailAPIView(RetrieveAPIView):
    queryset = Team.objects.select_related().filter(id__gte=0)
    serializer_class = TeamDetailSerializer

class TeamUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Team.objects.select_related().all()
    serializer_class = TeamSerializer