from django.http import HttpResponse
from .models import Photo, Hashtag
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View


class IndexListView(ListView):
    model = Photo
    template_name = "memories/index.html"
    context_object_name = "photos"

    def get_queryset(self):
        return Photo.objects.prefetch_related("hashtags")


class PhotoCreateView(View):
    def get(self, request):
        return render(request, "memories/new_photo.html")

    def post(self, request):
        if request.method == "POST":
            try:
                photo = request.FILES.get("photo")
                caption = request.POST.get("caption")
                hashtag_text = request.POST.get("hashtags")
                new_photo = Photo.objects.create(
                    photo=photo,
                    caption=caption,
                    sender="niloofar",
                )
                hashtag_names = [tag for tag in hashtag_text.split() if tag]
                for name in hashtag_names:
                    tag, created = Hashtag.objects.get_or_create(name=name)
                    new_photo.hashtags.add(tag)

                return redirect("IndexListView")

            except Exception as e:
                print("Error while saving:", e)
                return redirect("IndexListView")

        return render(request, "memories/new_photo.html")
