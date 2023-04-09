
from django.urls import path
from company import views

urlpatterns = [
    path(
        'company',
        views.CompanyListView.as_view(),
        name="company_list_view"),
    path(
        'company/<int:pk>',
        views.CompanyDetailView.as_view(),
        name="company_detail_view"),
    path(
        'company/create',
        views.CompanyFormView.as_view(),
        name="company_create_view"),
]
