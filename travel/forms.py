from django import forms
from .models import OrderPlaces

class OrderPlaceForm(forms.ModelForm):
    class Meta:
        model = OrderPlaces
        fields = ['full_name', 'phone_number',]

