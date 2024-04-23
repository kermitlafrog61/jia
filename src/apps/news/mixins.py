from . import models


class NewsViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_news'] = models.News.objects.all()
        context['news_tag'] = []
        for tag in models.NewsTag.objects.all():
            news_count = models.News.objects.filter(tag=tag).count()
            context['news_tag'].append(
                {'id': tag.id, 'title': tag.title, 'count': news_count})
        return context
