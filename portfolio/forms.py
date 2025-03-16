from django import forms
from django.core.mail import send_mail
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        send_mail(
            subject=f"Message from {name}",
            message=message,
            from_email=email,
            recipient_list=['your-email@example.com'],  # Update with your email
        )
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']