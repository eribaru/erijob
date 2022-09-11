from rest_framework.routers import DefaultRouter
#from api.views import UsuarioViewSet
from api.views import EmpresaViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
#router.register(r'usuarios', UsuarioViewSet)
router.register(r'empresa', EmpresaViewSet)

urlpatterns = router.urls