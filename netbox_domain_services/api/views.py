from netbox.api.viewsets import NetBoxModelViewSet
from .. import models
from .serializers import WebsiteSerializer, RegistrarSerializer, HosterSerializer


class WebsiteViewSet(NetBoxModelViewSet):
    queryset = models.Website.objects.prefetch_related('tags')
    serializer_class = WebsiteSerializer

class RegistrarViewSet(NetBoxModelViewSet):
    queryset = models.Registrar.objects.prefetch_related('tags')
    serializer_class = RegistrarSerializer

class HosterViewSet(NetBoxModelViewSet):
    queryset = models.Hoster.objects.prefetch_related('tags')
    serializer_class = HosterSerializer