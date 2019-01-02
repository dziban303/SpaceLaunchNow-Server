from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from api.models import *
from api.permission import HasGroupPermission
from api.v330.astronaut.filters import AstronautsFilter
from api.v330.astronaut.serializers import AstronautDetailedSerializer, AstronautListSerializer, AstronautNormalSerializer


# TODO docs
class AstronautViewSet(ModelViewSet):
    """
    API endpoint that allows Astronauts to be viewed.

    GET:
    Return a list of all the existing spacecraft.
    """
    queryset = Astronauts.objects.all()
    permission_classes = [HasGroupPermission]
    permission_groups = {
        'retrieve': ['_Public'], # retrieve can be accessed without credentials (GET 'site.com/api/foo/1')
        'list': ['_Public'] # list returns None and is therefore NOT accessible by anyone (GET 'site.com/api/foo')
    }

    def get_serializer_class(self):
        print(self.request.query_params.keys())
        mode = self.request.query_params.get("mode", "normal")
        if mode == "detailed" or self.action == 'retrieve':
            return AstronautDetailedSerializer
        elif mode == "list":
            return AstronautListSerializer
        else:
            return AstronautNormalSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = AstronautsFilter
    search_fields = ('$name', 'nationality', 'agency__name')
    ordering_fields = ('name', 'status', )