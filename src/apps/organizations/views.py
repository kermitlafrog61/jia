from django.views import generic

from . import models


class OrganizationDetailView(generic.DetailView):
    model = models.Organization
    template_name = 'content/organization.html'
    context_object_name = 'organization'
