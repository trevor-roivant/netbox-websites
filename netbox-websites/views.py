from netbox.views import generic
from . import forms, models, tables
from utilities.views import ViewTab, register_model_view

#Websites
class WebsiteView(generic.ObjectView):
    queryset = models.Website.objects.all()

class WebsiteListView(generic.ObjectListView):
    queryset = models.Website.objects.all()
    table = tables.WebsiteTable

class WebsiteEditView(generic.ObjectEditView):
    queryset = models.Website.objects.all()
    form = forms.WebsiteForm

class WebsiteDeleteView(generic.ObjectDeleteView):
    queryset = models.Website.objects.all()

#Registrars
class RegistrarView(generic.ObjectView):
    queryset = models.Registrar.objects.all()


class RegistrarListView(generic.ObjectListView):
    queryset = models.Registrar.objects.all()
    table = tables.RegistrarTable

class RegistrarEditView(generic.ObjectEditView):
    queryset = models.Registrar.objects.all()
    form = forms.RegistrarForm

class RegistrarDeleteView(generic.ObjectDeleteView):
    queryset = models.Registrar.objects.all()

#Hosters
class HosterView(generic.ObjectView):
    queryset = models.Hoster.objects.all()

class HosterListView(generic.ObjectListView):
    queryset = models.Hoster.objects.all()
    table = tables.HosterTable

class HosterEditView(generic.ObjectEditView):
    queryset = models.Hoster.objects.all()
    form = forms.HosterForm

class HosterDeleteView(generic.ObjectDeleteView):
    queryset = models.Hoster.objects.all()
