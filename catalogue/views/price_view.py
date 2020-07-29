from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from catalogue.models import Price, Product
from catalogue.forms import PriceForm


class PriceCreateView(LoginRequiredMixin, CreateView):
    model = Price
    form_class = PriceForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form_kwargs = self.get_form_kwargs()
        form_kwargs['initial'] = {'product':self.kwargs['product_id']}
        form_obj = form_class(**form_kwargs)
        return form_obj

    def get_success_url(self):
        return reverse_lazy('catalogue-product-detail',args=(self.kwargs['product_id'],))

