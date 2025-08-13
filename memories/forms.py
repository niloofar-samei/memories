from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = (
            "photo",
            "caption",
            "hashtag_list",
        )
        exclude = (
            "sender",
            "published_at",
        )

        labels = {
            "photo": "Photo",
            "caption": "Caption",
            "hashtag_list": "Hashtags",
        }
