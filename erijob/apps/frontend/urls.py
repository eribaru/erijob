from django.urls import include, path
from django.views.generic import TemplateView

from erijob.apps.frontend import views

app_name = 'frontend'

urlpatterns = [

    # path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='Index'),  # new
    path('login', TemplateView.as_view(template_name='login.html'), name='Login'),  # new
]
