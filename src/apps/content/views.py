from django.views import generic

from organizations.models import Organization
from . import models


class MainView(generic.TemplateView):
    template_name = 'content/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_pages'] = models.MainPageBanner.objects.all()
        context['contacts'] = models.Contact.objects.all()
        context['adverts'] = models.Advertising.objects.all()
        context['clubs'] = Organization.objects.filter(category='CLUB')
        context['committees'] = Organization.objects.filter(
            category='COMMITTEE')
        context['business'] = models.BusinessSupport.objects.all()
        return context


class MemberShipView(generic.ListView):
    model = models.MemberShip
    template_name = 'content/membership.html'
    context_object_name = 'members'


class ContactView(generic.DetailView):
    model = models.Contact
    template_name = 'content/contacts.html'
    context_object_name = 'contact'


class ReportsView(generic.ListView):
    model = models.Report
    template_name = 'content/reports.html'
    context_object_name = 'reports'


class ActionPlanView(generic.ListView):
    model = models.ActionPlane
    template_name = 'content/action-plan.html'
    context_object_name = 'action_plans'


class BusinessSupportView(generic.ListView):
    model = models.BusinessSupport
    template_name = 'content/business-support.html'
    context_object_name = 'business'


class SituationView(generic.ListView):
    model = models.Situation
    template_name = 'content/situation.html'
    context_object_name = 'situations'
