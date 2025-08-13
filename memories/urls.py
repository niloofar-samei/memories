from django.urls import path
from . import views
from memories.views import IndexListView

urlpatterns = [
    path("", IndexListView.as_view(), name="IndexListView"),
]
