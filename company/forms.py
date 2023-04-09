from django import forms
from django.forms import ModelForm
from .models import Company


class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

    name = forms.CharField(
        label="Nombre",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Apple Inc."}))
    domain = forms.CharField(
        label="Dominio",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "apple.com"}))
    industry = forms.CharField(
        label="Industria",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Technology"}))

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if 'class' in visible.field.widget.attrs:
                visible.field.widget.attrs['class'] = f'{visible.field.widget.attrs["class"]} form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
