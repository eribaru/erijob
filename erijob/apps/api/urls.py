from rest_framework.routers import DefaultRouter
from erijob.apps.api.views import EmpresaViewSet, CidadeViewSet, FormacaoViewSet, ExperienciaViewSet, \
    StatusEntrevistaViewSet, StatusInscricaoViewSet, InscricaoViewSet, VagaViewSet, UsuarioViewSet, \
    CurriculoViewSet, CreateUserView, EntrevistaViewSet, EnderecoViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'contas/registrar/', CreateUserView)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'entrevistas', EntrevistaViewSet)
router.register(r'curriculos', CurriculoViewSet)
router.register(r'formacoes', FormacaoViewSet)
router.register(r'experiencias', ExperienciaViewSet)
router.register(r'statusEntrevista', StatusEntrevistaViewSet)
router.register(r'statusInscricao', StatusInscricaoViewSet)
router.register(r'inscricoes', InscricaoViewSet)
router.register(r'vagas', VagaViewSet)

urlpatterns = router.urls
