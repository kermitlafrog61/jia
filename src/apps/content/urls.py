from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('membership/', views.MemberShipView.as_view(), name='membership'),
    path('business-support/', views.BusinessSupportView.as_view(),
         name='business_support'),
    path('action-plan/', views.ActionPlanView.as_view(), name='action_plan'),
    path('situation/', views.SituationView.as_view(), name='situation'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('contacts/<int:pk>/', views.ContactView.as_view(), name='contacts'),
]
