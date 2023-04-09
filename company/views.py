from django.shortcuts import render
from company import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class CompanyListView(LoginRequiredMixin, ListView):

    model = models.Company


class CompanyDetailView(LoginRequiredMixin, DetailView):

    model = models.Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyFormView(LoginRequiredMixin, CreateView):

    model = models.Company
    fields = "__all__"
