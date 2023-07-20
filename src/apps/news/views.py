from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from . import models, mixins


class NewsListView(mixins.NewsViewMixin, generic.ListView):
    model = models.News
    template_name = 'content/news.html'
    context_object_name = 'news'
    slug_field = 'slug'
    paginate_by = 4


class NewsDetailView(mixins.NewsViewMixin, generic.DetailView):
    model = models.News
    template_name = 'content/news_detail.html'
    context_object_name = 'news'


def get_news_data(request, tag_id):
    related_news = models.News.objects.all()
    news_tag = []
    for tag in models.NewsTag.objects.all():
        news_count = models.News.objects.filter(tag=tag).count()
        news_tag.append({'id': tag.id, 'title': tag.title,
                        'count': news_count})
    queryset = models.News.objects.filter(tag=tag_id)
    return render(
        request=request,
        template_name='content/news.html',
        context={
            'news': queryset,
            'related_news': related_news,
            'news_tag': news_tag
        })


class NewsDataView(mixins.NewsViewMixin, generic.DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get(self.pk_url_kwarg)
        context['news'] = models.News.objects.filter(tag=tag_id)


class SearchNewsView(mixins.NewsViewMixin, generic.ListView):
    model = models.News
    template_name = 'content/news.html'
    context_object_name = 'news'
    paginate_by = 4

    def get_queryset(self):
        queryset = models.News.objects.all()
        qury_obj = self.request.GET.get('search')
        if qury_obj:
            queryset = models.News.objects.filter(
                Q(title__icontains=qury_obj)
            )
        return queryset
