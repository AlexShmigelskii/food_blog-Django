from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here!'}),
        }