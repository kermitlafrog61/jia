from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news_detail/<str:slug>/',
         views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:tag_id>/', views.get_news_data, name='filter_news'),
    path('search/', views.SearchNewsView.as_view(), name='search'),
]
