from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Photo, Hashtag

admin.site.register(Session)
admin.site.register(Photo)
admin.site.register(Hashtag)
