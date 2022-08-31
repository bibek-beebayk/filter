from lib2to3.pytree import Base
import django_filters
from django_filters.filterset import BaseFilterSet, remote_queryset
from django.conf import settings
from django_filters.filters import MultipleChoiceFilter
from .models import Video
from django.db import models


class VideoFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Video
        fields = ['title', 'country', 'genres', 'tags']