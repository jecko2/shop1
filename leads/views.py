from django.shortcuts import render
from .models import Lead, Agent
from django.views.generic import ListView, TemplateView

class HomePaveView(TemplateView):
    template_name = 'index.html'
    
    

def home_page(request):
    return render(request, 'leads/home.html')


def leads_list(request):
    leads = Lead.objects.all()
    
    context = {
        'leads': leads
    }
    return render(request, 'leads/leads_list.html', context)

def lead_detail(request, pk):
    agent = Agent.objects.get(id=pk)
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead, 'agent':agent,
    }
    return render(request, 'leads/leads_detail.html', context)
    