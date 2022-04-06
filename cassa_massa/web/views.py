from django.shortcuts import render
from django.views.generic import TemplateView


class PrivacyPolicyTemplateView(TemplateView):
    template_name = 'privacy_policy.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)