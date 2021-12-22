from django.urls import path
from . import views
app_name  = 'leads'

urlpatterns = [
    # path('', views.home_page, name='home'),
    path('', views.HomePaveView.as_view(), name='home'),
    path('leads/', views.leads_list, name='leads-list'),
    path('lead-detail/<int:pk>/', views.lead_detail, name='lead-detail')
]


