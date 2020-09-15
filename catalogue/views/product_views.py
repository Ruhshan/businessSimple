from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin

from catalogue.models import Product, Price


class ProductListView(LoginRequiredMixin, SearchableListMixin,
                      SortableListMixin, ListView):
    model = Product
    search_fields = ['name']
    sort_fields = ['name']
    paginate_by = 10


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        prices = Price.objects.filter(product=context['object'])
        context['prices'] = prices
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'unitName', 'category', 'vendor', 'remarks']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'unitName', 'category', 'vendor', 'remarks']
    template_name_suffix = '_update_form'
