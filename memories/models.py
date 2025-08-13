from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to="photos/")
    sender = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender
