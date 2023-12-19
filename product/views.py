from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Products
from django import forms
from .forms import ProductCreateForm, ProductUpdateForm


"""
    Django Generic Views
        1-> Display views
            i-> Listview
            ii-> DetailView
        2-> Editing views
            i-> CreateView
            ii-> UpdateView
            iii-> DeleteView
            iv-> FormView
"""


class ProductsListView(generic.ListView):
    """
    Generic ListView:
    model: name of the model to be used
     --> this is enough for the view to work if template product_list.html exists
      and context will be by default product_list

    template_name: user defined template_name will override the default template by default modelname_list.html
    context_object_name: used to override default modelname_list name
    ordering: used for ordering will be overridden by get_queryset()

    get_queryset(): function to get the queryset
    get_context_data(): function to add additional context
    """

    model = Products
    template_name = 'products_list.html'
    context_object_name = 'products'  # by default will be products_list
    # template_name_suffix = '_list' # used to add a suffix to template
    # ordering = ['name']  # this will be overridden by get_queryset

    def get_queryset(self):
        """
        used to get the query set if we dont need all the data
        """
        return Products.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        """
        used to add additional data to the context object to be used in templates
        """
        context = super().get_context_data(*args, **kwargs)
        context['heading'] = {'headname': 'Shoppers'}
        return context

    def get_template_names(self):
        """
        used to add templates dynamically based on some conditions
        if superuser:
            return 'super_user.html'
        else:
            return self.template_name.html
        """
        return self.template_name


class ProductDetailView(generic.DetailView):
    """
        Django generic detail view
        path should be product/int<pk> (default) can be changed by pk_url_kwarg
    """
    model = Products
    template_name = 'products_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.model.objects.all().order_by('name')
        return context


class ProductCreateViewDefaultForm(generic.CreateView):
    """
        Django Generic Create View, it has a default form built in.
    """
    model = Products
    fields = ['name', 'description', 'price']
    template_name = 'products_create.html'

    def get_form(self):
        """
            used to get the form details to modify the form
        :return: form
        """
        form = super(ProductCreateViewDefaultForm, self).get_form()
        form.fields['description'].widget = forms.Textarea(attrs={'class': 'product_description'})
        return form

    def get_success_url(self):
        """
            is called after the code runs successfully
        :return:
        """
        return reverse('products_list')


class ProductCreateView(generic.CreateView):
    """
        Django generic Create view using a model Form
        form_class: the user defined form to be used, overrides the default form.
    """
    form_class = ProductCreateForm
    template_name = 'products_create.html'

    def get_success_url(self):
        return reverse('products_list')


class ProductUpdateView(generic.UpdateView):
    """
        Django Update view is almost same as a create view.
    """
    model = Products
    # fields = ['name', 'description', 'price'] # to be used if we use default form
    form_class = ProductUpdateForm
    template_name = 'product_update.html'

    def get_success_url(self):
        return reverse('products_list')


class ProductDeleteView(generic.DeleteView):
    """
        Django generic Delete View
    """
    model = Products
    template_name = 'products_delete.html'

    def get_success_url(self):
        return reverse('products_list')


def home(request):
    return render(request, 'home.html')
