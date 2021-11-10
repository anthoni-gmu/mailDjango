from django import forms
from .models import NewsletterUser, Newsletter


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']


class NewsletterCreateForm(forms.ModelForm):
    class Meta:
        models = Newsletter
        fields = ['name',
                  'subject',
                  'body',
                  'email' ]
