from django import forms
from .models import Message
class ContactForm(forms.ModelForm):
    name= forms.CharField(
        max_length=254,
        required=True,

    )
    mail = forms.EmailField(
        max_length=254,
        required=True,

    )
    subject = forms.CharField(
        max_length=254,
        required=True,

    )
    message = forms.CharField(
        max_length=254,
        widget=forms.Textarea(),
        required=True,
    )
    class Meta:
        model = Message
        fields = ['name', 'mail', 'message','subject']