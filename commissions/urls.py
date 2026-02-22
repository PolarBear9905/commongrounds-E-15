from django.urls import path
from .views import index, RequestListView, RequestDetailView

urlpatterns = [
    path('', index, name='index'),
    path(
        'requests/',
        RequestListView.as_view(),
        name='request_list'
    ),
    path(
        'request/<int:request_id>/',
        RequestDetailView.as_view(),
        name='request_detail'
    ),
]
