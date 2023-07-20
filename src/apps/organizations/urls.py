from django.urls import path

from . import views


urlpatterns = [
    path('organization/<int:pk>/',
         views.OrganizationDetailView.as_view(), name='organization'),
]
