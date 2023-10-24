from extras.plugins import PluginMenu , PluginMenuItem, PluginMenuButton
from utilities.choices import ButtonColorChoices

website_menu_items =   ( 
    PluginMenuItem(
        link='plugins:netbox_domain_services:website_list',
        link_text='Websites',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_domain_services:website_add',
                title='Websites',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,

            ),
        ),
    ),
    )
providers_menu_items =   ( 
    PluginMenuItem(
        link='plugins:netbox_domain_services:registrar_list',
        link_text='Registrars',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_domain_services:registrar_add',
                title='Registrars',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,


        ),
    ),
    ),
    PluginMenuItem(
        link='plugins:netbox_domain_services:hoster_list',
        link_text='Hosters',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_domain_services:hoster_add',
                title='Hosters',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,


        ),
    ),
    ),
    PluginMenuItem(
        link='plugins:netbox_domain_services:designer_list',
        link_text='Designers',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_domain_services:designer_add',
                title='Designers',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,


        ),
    ),
    ),
    PluginMenuItem(
        link='plugins:netbox_domain_services:developer_list',
        link_text='Developers',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_domain_services:developer_add',
                title='Developers',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,


        ),
    ),
    ),
)


menu = PluginMenu(
    label='Domain Services',
    groups=(
        ('Websites', website_menu_items),
       ('Providers', providers_menu_items), 
    ),
    icon_class='mdi mdi-dns'
)