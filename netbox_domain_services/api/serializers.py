from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Hoster, Website, Registrar


class NestedWebsiteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services:netbox_websites-api:website-detail'
    )

    class Meta:
        model = Website
        fields = ('id', 'url', 'display', 'name')


class WebsiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services-api:website-detail'
    )
    class Meta:
        model = Website
        fields = (
            'id', 'url', 'name', 'display', 'tenant','registrar', 'comments', 'hoster','contactgroup','url','status', 'tags', 'created',
            'last_updated',
        )
        


class NestedRegistrarSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services-api:registrar-detail'
    )

    class Meta:
        model = Registrar
        fields = ('id', 'url', 'display', 'name')



class RegistrarSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services-api:registrar-detail'
    )
    class Meta:
        model = Registrar
        fields = (
            'id', 'url', 'name', 'contactgroup', 'tags', 'created',
            'last_updated',
        )

class NestedHosterSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services-api:hoster-detail'
    )

    class Meta:
        model = Hoster
        fields = ('id', 'url', 'display', 'name')



class HosterSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_domain_services-api:hoster-detail'
    )
    class Meta:
        model = Hoster
        fields = (
            'id', 'url', 'name', 'contactgroup', 'tags', 'created',
            'last_updated',
        )
                