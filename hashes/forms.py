from django import forms
from .models import Document
from django.core.exceptions import ValidationError


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

    # Check fo 10 KBs restriction. 10240 bytes = 10 * 1024Bytes = 10KBs
    def clean(self):
        if(self.cleaned_data.get('document')).size > 10240:
            raise ValidationError("File size must be < 10KBs. Try another:")
        return self.cleaned_data
