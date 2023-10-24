from netbox.api.viewsets import NetBoxModelViewSet
from .. import models
from .serializers import WebsiteSerializer, RegistrarSerializer, HosterSerializer, DesignerSerializer, DeveloperSerializer


class WebsiteViewSet(NetBoxModelViewSet):
    queryset = models.Website.objects.prefetch_related('tags')
    serializer_class = WebsiteSerializer

class RegistrarViewSet(NetBoxModelViewSet):
    queryset = models.Registrar.objects.prefetch_related('tags')
    serializer_class = RegistrarSerializer

class HosterViewSet(NetBoxModelViewSet):
    queryset = models.Hoster.objects.prefetch_related('tags')
    serializer_class = HosterSerializer

class DesignerViewSet(NetBoxModelViewSet):
    queryset = models.Designer.objects.prefetch_related('tags')
    serializer_class =DesignerSerializer

class DeveloperViewSet(NetBoxModelViewSet):
    queryset = models.Developer.objects.prefetch_related('tags')
    serializer_class = DeveloperSerializer