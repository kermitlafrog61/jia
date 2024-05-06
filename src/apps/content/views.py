from django.views import generic

from apps.about.models import Branch

from . import models


class MainView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_pages'] = models.MainPageBanner.objects.all()
        context['branches'] = Branch.objects.all()
        context['adverts'] = models.Advertising.objects.all()
        context['clubs'] = models.Organization.objects.filter(category='CLUB')
        context['committees'] = models.Organization.objects.filter(
            category='COMMITTEE')
        context['business'] = models.BusinessSupport.objects.all()
        return context


class MemberShipView(generic.ListView):
    model = models.MemberShip
    template_name = 'membership.html'
    context_object_name = 'members'


class BranchView(generic.DetailView):
    model = Branch
    template_name = 'branches.html'
    context_object_name = 'branch'


class ReportsView(generic.ListView):
    model = models.Report
    template_name = 'reports.html'
    context_object_name = 'reports'


class ActionPlanView(generic.ListView):
    model = models.ActionPlane
    template_name = 'action-plan.html'
    context_object_name = 'action_plans'


class BusinessSupportView(generic.ListView):
    model = models.BusinessSupport
    template_name = 'business-support.html'
    context_object_name = 'business'


class SituationView(generic.ListView):
    model = models.Situation
    template_name = 'situation.html'
    context_object_name = 'situations'


class OrganizationDetailView(generic.DetailView):
    model = models.Organization
    template_name = 'organization.html'
    context_object_name = 'organization'
