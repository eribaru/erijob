from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from knox import views as knox_views
from erijob.apps.api.views import LoginView

# Serializers define the API representation.

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include('erijob.apps.api.urls', namespace='erijob.apps.api')),
    path(r'api/auth/', include('knox.urls')),
    path('admin/', admin.site.urls),
    path(r'login/', csrf_exempt(LoginView.as_view())),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
