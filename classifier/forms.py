from django import forms
from .models import SampleImage

class ImageForm(forms.ModelForm):
    class Meta:
        model = SampleImage
        fields = ['sample']
        labels = {'sample':''}