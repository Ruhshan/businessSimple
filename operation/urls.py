from django.urls import path
from operation.views import ReceiveListView, ReceiveCreateView

urlpatterns = [
    path('receive/list', ReceiveListView.as_view(), name='operation-receive-list'),
    path('receive/create', ReceiveCreateView.as_view(), name='operation-receive-create')

]