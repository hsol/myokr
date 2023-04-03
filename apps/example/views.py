from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class ExamplePageView(TemplateView):
    template_name = "page.html"
