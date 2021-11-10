from django.shortcuts import render
from .forms import NewsletterUserSignUpForm,NewsletterCreateForm
from .models import NewsletterUser
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
# Create your views here.
def newsletter_signup(request):
    form=NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,"Email already exists")
        else:
            instance.save()
            messages.success(request,"Hemos enviado un correo electronico a tu correo")
            #correo electronico
            subject="Libro de cocina"
            from_email=settings.EMAIL_HOST_USER
            to_email=[instance.email]
            
            html_template='newsletters/email/welcome.html'
            html_message=render_to_string(html_template)
            message=EmailMessage(subject,html_message,from_email,to_email)
            message.content_subtype='html'
            message.send()
    context={
        'form':form
    }
    return render(request,'start-here.html',context)

def newletter_unsubscribe(request):
    form=NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,"Email eliminado exists")
        else:
            print('Mensaje no encontrado')
            messages.warning(request,"Email not found")    
    context={
        'form':form
    }
    return render(request,'unsubscribe.html',context)
    