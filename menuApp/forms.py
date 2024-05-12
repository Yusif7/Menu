from django import forms

from .models import Item


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['meal', 'description', 'price', 'meal_type', 'author', 'status']



