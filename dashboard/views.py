from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from newsletters.models import Newsletter
class DashboardHomeView(TemplateView):
    template_name="dashboard/index.html"
    
class NewLettersDashboardHomeView(View):
    
    def get(self,request,*args,**kwargs):
        newletters=Newsletter.objects.all()
        context={
            'newletters':newletters
        }
        return render(request,'dashboard/list.html',context) 
    