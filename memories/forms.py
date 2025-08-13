from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("photo", "caption", "hashtag_list")
        exclude = ("sender", "published_at")

        labels = {
            "photo": "photo",
            "caption": "caption",
            "hashtag_list": "hashtag list",
        }
