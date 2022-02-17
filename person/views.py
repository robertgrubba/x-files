from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
# Create your views here.

class PersonListView(ListView):
    model = models.Person
    paginate_by = 10

class PersonDetailView(LoginRequiredMixin,DetailView):
    model = models.Person
    template_name = 'person/person_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context
