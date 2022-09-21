from django.urls import include, path
from django.views.generic import TemplateView

app_name = 'frontend'

urlpatterns = [


    path('', TemplateView.as_view(template_name='index.html'), name='Index'), # new
    path('login', TemplateView.as_view(template_name='login.html'), name='Login'), # new
]
