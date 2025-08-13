from django.urls import path
from . import views
from memories.views import IndexListView, PhotoCreateView

urlpatterns = [
    path("", IndexListView.as_view(), name="IndexListView"),
    path("new/", PhotoCreateView.as_view(), name="PhotoCreateView"),
]
