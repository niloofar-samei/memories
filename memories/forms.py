from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo",)
        exclude = ("sender", "published_at")

        labels = {"photo": "photo"}
