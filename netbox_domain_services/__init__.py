from extras.plugins import PluginConfig

class NetBoxDomainServicesConfig(PluginConfig):
    name = 'netbox_domain_services'
    verbose_name = 'NetBox Domain Services'
    description = 'Domain Services'
    version = '0.2'
    base_url = 'domain-services'
config = NetBoxDomainServicesConfig
