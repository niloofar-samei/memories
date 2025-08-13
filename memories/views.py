from django.http import HttpResponse
from .models import Photo
from django.views.generic import ListView
from django.shortcuts import render
from django.views import View
from memories.forms import PhotoForm


class IndexListView(ListView):
    model = Photo
    template_name = "memories/index.html"
    context_object_name = "photos"


class PhotoCreateView(View):
    def get(self, request):
        return render(request, "memories/new_photo.html", {"photo_form": PhotoForm()})
