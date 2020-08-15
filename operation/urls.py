from django.urls import path

from base.logutil import Loggable
from operation.views import ReceiveListView, ReceiveCreateView, ReceiveDetailView, ReceiveUpdateView
from operation.views import IssueCreateView, IssueDetailView, IssueListView, IssueUpdateView
from operation.views import ReturnCreateView, ReturnDetailView, ReturnListView, ReturnUpdateView
from operation.views import DailySummaryListView


urlpatterns = [
    path('receive/list', ReceiveListView.as_view(), name='operation-receive-list'),
    path('receive/create', Loggable(ReceiveCreateView,True).as_view(), name='operation-receive-create'),
    path('receive/detail/<int:pk>', Loggable(ReceiveDetailView,True).as_view(), name='operation-receive-detail'),
    path('receive/update/<int:pk>', ReceiveUpdateView.as_view(), name='operation-receive-update'),

    path('issue/list', IssueListView.as_view(), name='operation-issue-list'),
    path('issue/create', IssueCreateView.as_view(), name='operation-issue-create'),
    path('issue/detail/<int:pk>', IssueDetailView.as_view(), name='operation-issue-detail'),
    path('issue/update/<int:pk>', IssueUpdateView.as_view(), name='operation-issue-update'),

    path('return/create', ReturnCreateView.as_view(), name="operation-return-create"),
    path('return/detail/<int:pk>', ReturnDetailView.as_view(), name="operation-return-detail"),
    path('return/list', ReturnListView.as_view(), name='operation-return-list'),
    path('return/update/<int:pk>', ReturnUpdateView.as_view(), name='operation-return-update'),

    path('summary/list', DailySummaryListView.as_view(), name='daily-summary-list')
]

