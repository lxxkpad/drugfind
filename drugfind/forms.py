from typing_extensions import Required
from django import forms

class UploadForm(forms.Form):
    file = forms.ImageField(required=True)

class UploadImageForm(forms.Form):
    file = forms.ImageField(label='Image')
