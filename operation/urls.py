from django.urls import path
from operation.views import ReceiveListView, ReceiveCreateView, ReceiveDetailView, ReceiveUpdateView
from operation.views import IssueCreateView, IssueDetailView, IssueListView, IssueUpdateView

urlpatterns = [
    path('receive/list', ReceiveListView.as_view(), name='operation-receive-list'),
    path('receive/create', ReceiveCreateView.as_view(), name='operation-receive-create'),
    path('receive/detail/<int:pk>', ReceiveDetailView.as_view(), name='operation-receive-detail'),
    path('receive/update/<int:pk>', ReceiveUpdateView.as_view(), name='operation-receive-update'),

    path('issue/list', IssueListView.as_view(), name='operation-issue-list'),
    path('issue/create', IssueCreateView.as_view(), name='operation-issue-create'),
    path('issue/detail/<int:pk>', IssueDetailView.as_view(), name='operation-issue-detail'),
    path('issue/update/<int:pk>', IssueUpdateView.as_view(), name='operation-issue-update')
]