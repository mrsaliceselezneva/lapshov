from .models import Therm
from django.forms import ModelForm, TextInput, Textarea, ImageField


class ThermForm(ModelForm):
    class Meta:
        model = Therm
        fields = ['title', 'body', 'image', 'mark']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'название'
            }),
            'body': Textarea(attrs={
                'placeholder': 'определение'
            }),
            'mark': TextInput(attrs={
                'placeholder': 'обозначение'
            }),
        }
