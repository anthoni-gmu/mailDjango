from django import forms
from .models import NewsletterUser, Newsletter


class NewsletterUserSignUpForm(forms.ModelForm):
    class meta:
        model = NewsletterUser
        fields = ['email']


class NewsletterCreateForm(forms.ModelForm):
    class meta:
        models = Newsletter
        fields = ['name',
                  'subject',
                  'body',
                  'email' ]
