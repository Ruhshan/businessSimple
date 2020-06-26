from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class VendorCreateView(LoginRequiredMixin, CreateView):
        model = Vendor
        fields = ['name','phone','email','address','remarks']

class VendorUpdateView(LoginRequiredMixin, UpdateView):
        model = Vendor
        template_name_suffix = '_update_form'
        fields = ['name', 'phone', 'email', 'address', 'remarks']

