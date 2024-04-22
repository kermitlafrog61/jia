from django.views import generic

from ..content.models import Organization
from . import models


class AboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizations = Organization.objects.all()

        context['clubs'] = []
        context['committees'] = []
        for org in organizations:
            if org.category == 'COMMITTEE':
                context['committees'].append(org)
            elif org.category == 'CLUB':
                context['clubs'].append(org)
        return context


class TeamViewList(generic.ListView):
    model = models.GoverningBody
    template_name = 'team.html'
    context_object_name = 'teams'


class DirectionView(generic.TemplateView):
    template_name = 'direction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = models.TeamMember.objects.filter(
            choice='director')
        context['hrs'] = models.TeamMember.objects.filter(choice='hr')
        context['branches'] = models.Branch.objects.all()
        return context


class PartnersView(generic.ListView):
    model = models.State
    template_name = 'partners.html'
    context_object_name = 'partners'


class PartnershipView(generic.ListView):
    model = models.Partnership
    template_name = 'partnership.html'
    context_object_name = 'partnerships'


class ServiceView(generic.TemplateView):
    template_name = 'service.html'


class CorporateCultureView(generic.TemplateView):
    template_name = 'corporate-culture.html'


class JournalView(generic.ListView):
    model = models.Journal
    template_name = 'journals.html'
    context_object_name = 'journals'
    paginate_by = 10


class CharterView(generic.TemplateView):
    template_name = 'charter.html'
