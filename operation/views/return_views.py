from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin

from operation.models import Return


class ReturnCreateView(LoginRequiredMixin, CreateView):
    model = Return
    fields = ['product', 'unit', 'date', 'receipt_no', 'customer','remarks']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ReturnDetailView(LoginRequiredMixin, DetailView):
    model = Return


class ReturnListView(LoginRequiredMixin,
        SearchableListMixin,
        SortableListMixin,
        ListView):
    model = Return
    search_fields = ['product__name']
    sort_fields = ['date', 'product__name']
    paginate_by = 10


class ReturnUpdateView(LoginRequiredMixin, UpdateView):
    model = Return
    fields = ['product', 'unit', 'date', 'receipt_no', 'customer', 'remarks']
    template_name_suffix = '_update_form'
