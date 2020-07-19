from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from extra_views import SearchableListMixin, SortableListMixin

from operation.models import Issue
from operation.forms import IssueForm

class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue


class IssueListView(LoginRequiredMixin,
        SearchableListMixin,
        SortableListMixin,
        ListView):
    model = Issue
    search_fields = ['product__name']
    sort_fields = ['date', 'product__name']
    paginate_by = 10


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name_suffix = '_update_form'