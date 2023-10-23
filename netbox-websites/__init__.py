from extras.plugins import PluginConfig

class NetBoxWebsitesConfig(PluginConfig):
    name = 'netbox_websites'
    verbose_name = 'NetBox websites'
    description = 'Keep inventory of websites'
    version = '0.1'
    base_url = 'websites'
config = NetBoxWebsitesConfig
