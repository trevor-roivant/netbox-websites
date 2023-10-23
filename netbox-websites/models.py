from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from .choices import WebsiteStatusChoices
from django.urls import reverse

class Website(NetBoxModel):
    name = models.CharField(
        max_length=32
    )
    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )
    url = models.CharField(
        help_text='Website URL',
        max_length=32,
        unique = True
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=50,
        choices=AccountStatusChoices,
        default=AccountStatusChoices.STATUS_ACTIVE
    )
    contactgroup = models.ForeignKey(
        help_text='Account Owner',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    registrar = models.ForeignKey(
        help_text='Registrar',
        to='Registrar',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )
    hoster = models.ForeignKey(
        help_text='Hoster',
        to='Hoster',
        on_delete=models.PROTECT,
        related_name="+",
        blank=True,
        null=True
    )
    repo = models.CharField(
        max_length=200,
        blank=True
    )
    comments = models.TextField(
        blank=True
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_websites:website', args=[self.pk])
    def get_status_color(self):
        return WebsiteStatusChoices.colors.get(self.status)

class Registrar(NetBoxModel):
    name = models.CharField(
        max_length=32
    )
    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )
    contactgroup = models.ForeignKey(
        help_text='Account Group',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_websites:registrar', args=[self.pk])

class Hoster(NetBoxModel):
    name = models.CharField(
        max_length=32
    )
    display = models.CharField(
        max_length=32,
        blank=True,
        null=True
        )
    contactgroup = models.ForeignKey(
        help_text='Account Group',
        to='tenancy.contactgroup',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('plugins:netbox_websites:hoster', args=[self.pk])