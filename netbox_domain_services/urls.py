from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('websites/', views.WebsiteListView.as_view(), name='website_list'),
    path('websites/add/', views.WebsiteEditView.as_view(), name='website_add'),
    path('websites/<int:pk>/', views.WebsiteView.as_view(), name='website'),
    path('websites/<int:pk>/edit/', views.WebsiteEditView.as_view(), name='website_edit'),
    path('websites/<int:pk>/delete/', views.WebsiteDeleteView.as_view(), name='website_delete'),
    path('websites/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='website_changelog', kwargs={
        'model': models.Website
    }),
    path('registrar/', views.RegistrarListView.as_view(), name='registrar_list'),
    path('registrar/add/', views.RegistrarEditView.as_view(), name='registrar_add'),
    path('registrar/<int:pk>/', views.RegistrarView.as_view(), name='registrar'),
    path('registrar/<int:pk>/edit/', views.RegistrarEditView.as_view(), name='registrar_edit'),
    path('registrar/<int:pk>/delete/', views.RegistrarDeleteView.as_view(), name='registrar_delete'),
    path('registrar/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='registrar_changelog', kwargs={
        'model': models.Registrar
    }),
    path('hoster/', views.HosterListView.as_view(), name='hoster_list'),
    path('hoster/add/', views.HosterEditView.as_view(), name='hoster_add'),
    path('hoster/<int:pk>/', views.HosterView.as_view(), name='hoster'),
    path('hoster/<int:pk>/edit/', views.HosterEditView.as_view(), name='hoster_edit'),
    path('hoster/<int:pk>/delete/', views.HosterDeleteView.as_view(), name='hoster_delete'),
    path('hoster/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='hoster_changelog', kwargs={
        'model': models.Hoster
    }),
    path('designer/', views.DesignerListView.as_view(), name='designer_list'),
    path('designer/add/', views.DesignerEditView.as_view(), name='designer_add'),
    path('designer/<int:pk>/', views.DesignerView.as_view(), name='designer'),
    path('designer/<int:pk>/edit/', views.DesignerEditView.as_view(), name='designer_edit'),
    path('designer/<int:pk>/delete/', views.DesignerDeleteView.as_view(), name='designer_delete'),
    path('designer/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='designer_changelog', kwargs={
        'model': models.Designer
    }),
    path('developer/', views.DeveloperListView.as_view(), name='developer_list'),
    path('developer/add/', views.DeveloperEditView.as_view(), name='developer_add'),
    path('developer/<int:pk>/', views.DeveloperView.as_view(), name='developer'),
    path('developer/<int:pk>/edit/', views.DeveloperEditView.as_view(), name='developer_edit'),
    path('developer/<int:pk>/delete/', views.DeveloperDeleteView.as_view(), name='developer_delete'),
    path('developer/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='developer_changelog', kwargs={
        'model': models.Developer
    })
    
    
)