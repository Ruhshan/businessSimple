from django.urls import path
from operation.views import ReceiveListView, ReceiveCreateView, ReceiveDetailView, ReceiveUpdateView

urlpatterns = [
    path('receive/list', ReceiveListView.as_view(), name='operation-receive-list'),
    path('receive/create', ReceiveCreateView.as_view(), name='operation-receive-create'),
    path('receive/detail/<int:pk>', ReceiveDetailView.as_view(), name='operation-receive-detail'),
    path('receive/update/<int:pk>', ReceiveUpdateView.as_view(), name='operation-receive-update')
]