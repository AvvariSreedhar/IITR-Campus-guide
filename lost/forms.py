from django import forms
from .models import LostItem

class LostForm(forms.ModelForm):

    class Meta:

        model = LostItem
        widgets = {
            'title': forms.TextInput(attrs={
            'autocomplete': 'off', 
            'autofocus': 'on', 
            'class': 'form-control', 
            'placeholder': 'Enter title'
            }), 
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'autocomplete': 'off', 
                'placeholder': 'Enter description', 
                'rows': 3, 
            }), 
            'email_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'autocomplete': 'off', 
                'placeholder': 'name@example.com', 
                'width': '200px', 
            }), 
        }
        fields = [
            'title', 
            'description', 
            'email_id', 
            'picture', 
        ]