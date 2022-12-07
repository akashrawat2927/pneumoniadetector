from django.contrib import admin
from .models import SampleImage
# Register your models here.

@admin.register(SampleImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sample']
