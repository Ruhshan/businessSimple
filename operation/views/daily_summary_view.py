from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from extra_views import SearchableListMixin, SortableListMixin

from operation.models import DailySummary

class DailySummaryListView(LoginRequiredMixin,
        SearchableListMixin,
        SortableListMixin,
        ListView):
    model = DailySummary
    search_fields = ['product__name']
    sort_fields = ['date', 'product__name']
    paginate_by = 10
