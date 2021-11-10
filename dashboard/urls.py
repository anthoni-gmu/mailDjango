from django.urls import path
from .views import DashboardHomeView,NewLettersDashboardHomeView
app_name='dashboard'

urlpatterns = [
    path('',DashboardHomeView.as_view(),name="home"),
    path('list/',NewLettersDashboardHomeView.as_view(),name="list")
    
]
