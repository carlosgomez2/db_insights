from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView


class CompanyListView(LoginRequiredMixin, ListView):

    model = Company
    context_object_name = "companies"
    paginate_by = 15


class CompanyDetailView(LoginRequiredMixin, DetailView):

    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyFormView(LoginRequiredMixin, CreateView):

    model = Company
    fields = "__all__"


class CompanyUpdateView(LoginRequiredMixin, UpdateView):

    model = Company
    fields = "__all__"
