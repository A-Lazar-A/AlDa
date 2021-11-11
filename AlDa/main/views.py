from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PassportOfObject


class MainTemplateView(TemplateView):
    template_name = 'main/index.html'
    table = PassportOfObject

    def get_context_data(self, **kwargs):
        kwargs['Objects'] = PassportOfObject.objects.order_by('-id')
        return super().get_context_data(**kwargs)


# Create your views here.
