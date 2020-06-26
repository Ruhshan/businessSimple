from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from extra_views import SearchableListMixin, SortableListMixin
from catalogue.models import Vendor

class VendorListview(LoginRequiredMixin,
        SearchableListMixin,
        SortableListMixin,
        ListView):
        model = Vendor
        search_fields = ['name','phone']
        sort_fields = ['name','phone']
        paginate_by = 10


class VendorDetailView(LoginRequiredMixin, DetailView):
        model = Vendor


