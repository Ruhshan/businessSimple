from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from catalogue.models import Price, Product
from catalogue.forms import PriceForm
from django.http import JsonResponse
from django.db.models import F



class PriceCreateView(LoginRequiredMixin, CreateView):
    model = Price
    form_class = PriceForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form_kwargs = self.get_form_kwargs()
        form_kwargs['initial']['product'] = self.kwargs['product_id']
        form_obj = form_class(**form_kwargs)
        return form_obj

    def get_success_url(self):
        return reverse_lazy('catalogue-product-detail',args=(self.kwargs['product_id'],))


class PriceUpdateView(LoginRequiredMixin, UpdateView):
    model = Price
    form_class = PriceForm
    template_name_suffix = "_update_form"

    def get_context_data(self, **kwargs):
        context = super(PriceUpdateView,self).get_context_data(**kwargs)
        product_name = Product.objects.get(id=self.kwargs['product_id']).name
        context['product_name'] = product_name
        return context

    def get_success_url(self):
        return reverse_lazy('catalogue-product-detail',args=(self.kwargs['product_id'],))

def get_price_for_product(request,product_id):
    prices = Price.objects.filter(product_id=product_id, isActive=True)\
        .values("id","buying","selling")

    return JsonResponse(list(prices),safe=False)
