import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Website, Registrar, Hoster

class WebsiteTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    status = ChoiceFieldColumn()
    class Meta(NetBoxTable.Meta):
        model = Website
        fields = ('pk', 'id', 'name','url','repo','hoster', 'tenant','status')
        default_columns = ('name', 'url','tenant','status')

class RegistrarTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Registrar
        fields = ('pk', 'id', 'name')
        default_columns = ('name',)

class HosterTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = Hoster
        fields = ('pk', 'id', 'name')
        default_columns = ('name',)