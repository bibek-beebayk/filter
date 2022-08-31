from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import CountrySerializer, GenreSerializer, TagSerializer, VideoListSerializer, VideoDetailSerializer
from .filters import VideoFilter
from .models import Video, Tag, Genre, Country


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().select_related('country').prefetch_related('tags', 'genres')
    serializer_class = VideoDetailSerializer



    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = VideoListSerializer
        return self.serializer_class


class FilterSelectViewSet(viewsets.GenericViewSet):

    tags = TagSerializer(Tag.objects.all(), many=True).data
    genres = GenreSerializer(Genre.objects.all(), many=True).data
    countries = CountrySerializer(Country.objects.all(), many=True).data

    def list(self, request):
        res = {
            'tags': self.tags,
            'genres': self.genres,
            'countries': self.countries
        }
        return Response(res)

class FilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    
    filter_data = {
        'tags': {
            1 : False,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
            6 : False,
            7 : False,
            8 : False,
        },
        'genres': {
            1 : True,
            2 : False,
            3 : False,
            4 : False,
            5 : False,
        },
        # 'countries': {
        #     1 : True,
        #     2 : True,
        # }
    }

    filter_params = {}
    for key, value in filter_data.items():
        values = []       
        for k, v in value.items():
            if v:
                values.append(k)
        if values:
            filter_params[key] = values


    serializer_class = VideoDetailSerializer  

    # filterset_class = VideoFilter
    queryset = Video.objects.all().select_related('country').prefetch_related('tags', 'genres').filter(**filter_params).distinct()

    # queryset = Video.objects.all().select_related('country').prefetch_related('tags', 'genres')
    # filterset_fields = ('country', 'genres', 'tags')

