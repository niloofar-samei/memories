from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo_name",)

        labels = {"photo_name": "photo_name"}

        # This block helps to check if the new photo name already exists or not.
        # In class-based views, we have to use it to check.
        def clean_photo_name(self):
            name = self.cleaned_data["photo_name"]
            if Photo.objects.filter(photo_name__iexact=name).exists():
                raise form.ValidationError("Sorry but this photo already exists.")
            return name
