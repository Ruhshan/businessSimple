from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
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
        return super().form_valid(form)


class ReceiveDetailView(LoginRequiredMixin, DetailView):
    model = Receive


class ReceiveUpdateView(LoginRequiredMixin, UpdateView):
    model = Receive
    form_class = ReceiveForm
    template_name_suffix = '_update_form'


class ReceiveDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,'operation/test_template.html')

    def put(self, request):
        return HttpResponse("ok")