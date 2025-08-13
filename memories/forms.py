from django import forms
from .models import Photo


class PhotoForm(froms.ModelForm):
    class Meta:
        model = Photo
        fields = "photo_name"

        labels = {"photo_name": "photo_name"}

        # This block helps to check if the new movie name already exists or not.
        # In class-based views, we have to use it to check.
        def clean_movie_name(self):
            name = self.cleaned_data["movie_name"]
            if Movie.objects.filter(movie_name__iexact=name).exists():
                raise form.ValidationError("Sorry but this movie already exists.")
            return name
