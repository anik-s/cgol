from django.conf.urls import url

from grids.views import GridView, GridDetailView

urlpatterns = [
    url(r'^$', GridView.as_view(), name='grid-list'),
    url(r'^(?P<pk>[0-9]+)$', GridDetailView.as_view(), name='book-detail'),
]