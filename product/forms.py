from django import forms
from .models import Products


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price']
        widgets = {
            'description': forms.Textarea()
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price']
        widgets = {
            'description': forms.Textarea()
        }
