from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_domain_services'

router = NetBoxRouter()
router.register('website', views.WebsiteViewSet)
router.register('registrar', views.RegistrarViewSet)
router.register('hoster', views.HosterViewSet)
urlpatterns = router.urls