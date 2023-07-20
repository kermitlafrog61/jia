from django.urls import path

from . import views


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('team/', views.TeamViewList.as_view(), name='team'),
    path('direction/', views.DirectionView, name='direction'),
    path('partners/', views.PartnersView, name='partners'),
    path('partnership/', views.PartnershipView.as_view(), name='partnership'),
    path('services/', views.ServiceView, name='services'),
    path('corporate-culture/', views.CorporateCultureView,
         name='corporate-culture'),
    path('journals/', views.JournalView.as_view(), name='journals'),
    path('charter/', views.CharterView, name='charter'),
]
