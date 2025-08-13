from django.http import HttpResponse
from .models import Photo
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View


class IndexListView(ListView):
    model = Photo
    template_name = "memories/index.html"
    context_object_name = "photos"


class PhotoCreateView(View):
    def get(self, request):
        return render(request, "memories/new_photo.html")


#    def post(self, request):
#        photo_form = PhotoForm(request.POST, request.FILES)
#
#        if photo_form.is_valid():
#            p = photo_form.save(commit=False)
#            p.sender = "niloofar"
#            p.save()
#            return redirect("IndexListView")
#
#        return render(request, "memories/new_photo.html", {"photo_form": PhotoForm()})
