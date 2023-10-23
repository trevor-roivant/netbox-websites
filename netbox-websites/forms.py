from netbox.forms import NetBoxModelForm
from .models import Website, Registrar, Hoster
from django import forms
from tenancy.models import ContactGroup, Contact, Tenant
from utilities.forms.fields import (
    DynamicModelChoiceField, CSVModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField, CSVChoiceField,
)

class WebsiteForm(NetBoxModelForm):
    url = forms.CharField(
        required=True,
        label='URL'
    )
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        label='Tenant',
        required=False
    )
    registrar = DynamicModelChoiceField(
        queryset = Registrar.objects.all(),
        label ='Registrar',
        required = True
    )

    hoster = DynamicModelChoiceField(
        queryset = Hoster.objects.all(),
        label ='Hoster',
        required = True
    )
    class Meta:
        model = CloudAccount
        fields = ('name', 'url', 'status' , 'registrar', 'tenant','hoster', 'contactgroup')

class RegistrarForm(NetBoxModelForm):
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    class Meta:
        model = Registrar
        fields = ('name', 'contactgroup')

class HosterForm(NetBoxModelForm):
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    class Meta:
        model = Hoster
        fields = ('name', 'contactgroup')