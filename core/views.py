from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_at')

        return context
