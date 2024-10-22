from django.contrib import admin
from .models import Topic, Comment , Profile
# Register your models here.
admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Profile)