from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'phone', 'email', 'address',]

        widgets = {
            'fields': forms.TextInput(attrs={'class': 'field_class'}),
        }


