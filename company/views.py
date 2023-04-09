from company.models import Company
from company.forms import CompanyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import pdb


class CompanyListView(LoginRequiredMixin, ListView):

    # Same as model = Company; which means: Company.objects.all()
    queryset = Company.objects.order_by('-pk')
    context_object_name = "companies"
    paginate_by = 15


class CompanyDetailView(LoginRequiredMixin, DetailView):

    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CompanyFormView(LoginRequiredMixin, CreateView):

    model = Company
    form_class = CompanyForm


class CompanyUpdateView(LoginRequiredMixin, UpdateView):

    model = Company
    form_class = CompanyForm
