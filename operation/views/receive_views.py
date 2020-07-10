from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin

from operation.models import Receive


class ReceiveListView(LoginRequiredMixin,
        SearchableListMixin,
        SortableListMixin,
        ListView):
    model = Receive
    search_fields = ['product__name']
    sort_fields = ['date', 'product__name']
    paginate_by = 10


class ReceiveCreateView(LoginRequiredMixin, CreateView):
    model = Receive
    fields = ['product', 'unit', 'date', 'receipt_no']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ReceiveDetailView(LoginRequiredMixin, DetailView):
    model = Receive


class ReceiveUpdateView(LoginRequiredMixin, UpdateView):
    model = Receive
    fields = ['product', 'unit', 'date', 'receipt_no']
    template_name_suffix = '_update_form'