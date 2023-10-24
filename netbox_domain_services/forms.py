from netbox.forms import NetBoxModelForm
from .models import Website, Registrar, Hoster, Designer, Developer
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
    developer = DynamicModelChoiceField(
        queryset = Developer.objects.all(),
        label ='Developer',
        required = True
    )
    designer = DynamicModelChoiceField(
        queryset = Designer.objects.all(),
        label ='Designer',
        required = True
    )
    class Meta:
        model = Website
        fields = ('name', 'url', 'repo', 'status' , 'registrar','hoster','developer', 'designer', 'tenant', 'contactgroup')

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

class DesignerForm(NetBoxModelForm):
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    class Meta:
        model = Designer
        fields = ('name', 'contactgroup')

class DeveloperForm(NetBoxModelForm):
    contactgroup = DynamicModelChoiceField(
        queryset=ContactGroup.objects.all(),
        label='Contact Group',
        required=False
    )

    class Meta:
        model = Developer
        fields = ('name', 'contactgroup')