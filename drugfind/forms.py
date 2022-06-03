from typing_extensions import Required
from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(required=True)

class UPloadImageForm(forms.Form):
    file = forms.ImageField(label='Image')
