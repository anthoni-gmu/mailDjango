from django.urls import path 
from .views import newsletter_signup,newletter_unsubscribe

app_name="newsletters" 
urlpatterns=[
    path('entrenamiento/',newsletter_signup,name="optin"),
    path('unsubscribe/',newletter_unsubscribe,name="unsubscribe"),
    
]