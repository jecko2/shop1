
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('leads.urls', namespace='leads')),
]

admin.site.site_header = 'EVENING DJANG PRAC'
admin.site.site_title = 'DJANGO PRACTICE'
