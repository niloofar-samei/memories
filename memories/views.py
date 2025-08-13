from django.http import HttpResponse
from .models import Photo
from django.views.generic import ListView


class IndexListView(ListView):
    model = Photo
    template_name = "memories/index.html"
    context_object_name = "photos"
