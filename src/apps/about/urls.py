from django.urls import path

from . import views


urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('team/', views.TeamViewList.as_view(), name='team'),
    path('direction/', views.DirectionView.as_view(), name='direction'),
    path('partners/', views.PartnersView.as_view(), name='partners'),
    path('partnership/', views.PartnershipView.as_view(), name='partnership'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('corporate-culture/', views.CorporateCultureView.as_view(),
         name='corporate-culture'),
    path('journals/', views.JournalView.as_view(), name='journals'),
    path('charter/', views.CharterView.as_view(), name='charter'),
]
