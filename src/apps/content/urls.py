from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('branches/<int:pk>/', views.BranchView.as_view(), name='branches'),
    path('organization/<int:pk>/',
         views.OrganizationDetailView.as_view(), name='organization'),
    path('membership/', views.MemberShipView.as_view(), name='membership'),
    path('business_support/', views.BusinessSupportView.as_view(),
         name='business_support'),
    path('action_plan/', views.ActionPlanView.as_view(), name='action_plan'),
    path('situation/', views.SituationView.as_view(), name='situation'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
]
