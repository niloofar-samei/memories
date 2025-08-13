from django.db import models


class Photo(models.Model):
    photo_name = models.CharField(max_length=200, unique=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo_name
