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

    def post(self, request):
        if request.method == "POST":
            try:
                photo = request.FILES.get("photo")
                caption = request.POST.get("caption")
                hashtags = request.POST.get("hashtags")
                new_photo = Photo.objects.create(
                    photo=photo,
                    caption=caption,
                    hashtag_list=hashtags,
                    sender="niloofar",
                )
                return redirect("IndexListView")
            except Exception as e:
                print("Error while saving:", e)
                return redirect("IndexListView")

        return render(request, "memories/new_photo.html")
