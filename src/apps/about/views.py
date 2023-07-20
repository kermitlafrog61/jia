from django.views import generic

from ..organizations.models import Organization
from . import models


class AboutView(generic.TemplateView):
    template_name = 'content/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizations = Organization.objects.all()
        context['clubs'] = [
            org for org in organizations if org.category == 'CLUB']
        context['committees'] = [
            org for org in organizations if org.category == 'COMMITTEE']
        return context


class TeamViewList(generic.ListView):
    model = models.GoverningBody
    template_name = 'content/team.html'
    context_object_name = 'teams'


class DirectionView(generic.TemplateView):
    template_name = 'content/direction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = models.TeamMember.objects.filter(
            choice='director')
        context['hrs'] = models.TeamMember.objects.filter(choice='hr')
        context['branches'] = models.Branch.objects.all()


class PartnersView(generic.ListView):
    model = models.State
    template_name = 'content/partners.html'
    context_object_name = 'partners'


class PartnershipView(generic.ListView):
    model = models.Partnership
    template_name = 'content/partnership.html'
    context_object_name = 'partnerships'


class ServiceView(generic.TemplateView):
    template_name = 'content/service.html'


class CorporateCultureView(generic.TemplateView):
    template_name = 'content/corporate-culture.html'


class JournalView(generic.ListView):
    model = models.Journal
    template_name = 'content/journals.html'
    context_object_name = 'journals'
    paginate_by = 10


class CharterView(generic.TemplateView):
    template_name = 'content/charter.html'
