from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to="photos/")
    sender = models.CharField(max_length=100)
    caption = models.CharField(max_length=500)
    hashtags = models.ManyToManyField(Hashtag, related_name="photos")
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender
