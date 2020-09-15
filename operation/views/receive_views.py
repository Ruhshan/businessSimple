from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin
from operation.forms import ReceiveForm
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
    form_class = ReceiveForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.unit = int(form.instance.unitPerPackage) * int(form.instance.receivedPackage)
        return super().form_valid(form)


class ReceiveDetailView(LoginRequiredMixin, DetailView):
    model = Receive


class ReceiveUpdateView(LoginRequiredMixin, UpdateView):
    model = Receive
    form_class = ReceiveForm
    template_name_suffix = '_update_form'
