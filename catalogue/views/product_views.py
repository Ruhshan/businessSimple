from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin

from catalogue.models import Product


class ProductListView(LoginRequiredMixin, SearchableListMixin,
                      SortableListMixin, ListView):
    model = Product
    search_fields = ['name']
    sort_fields = ['name']
    paginate_by = 10


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'vendor', 'remarks']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'category', 'vendor', 'remarks']
    template_name_suffix = '_update_form'
