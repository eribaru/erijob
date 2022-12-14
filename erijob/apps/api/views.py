# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from httpie import status
from requests import Response
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from knox.views import LoginView as KnoxLoginView

from erijob.apps.api.models import Empresa, Cidade, Curriculo, InstituicaoEnsino, Formacao, StatusInscricao, \
    StatusEntrevista, Experiencia, Inscricao, Vaga, Usuario, Entrevista, Endereco
from erijob.apps.api.serializers import EmpresaSerializer, CidadeSerializer, \
    CurriculoSerializer, InstituicaoEnsinoSerializer, FormacaoSerializer, StatusInscricaoSerializer, \
    StatusEntrevistaSerializer, ExperienciaSerializer, InscricaoSerializer, VagaSerializer, UsuarioSerializer, \
    GroupSerializer, UsuarioCadastroSerializer, EntrevistaSerializer, EnderecoSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_fields = ['email']
    permission_classes = [permissions.IsAuthenticated]


class CreateUserView(CreateModelMixin, GenericViewSet):
    permission_classes = []
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCadastroSerializer


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

    def get_user_serializer_class(self):
        return UsuarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['sede', 'ramo']
    search_fields = ['nome']


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['cod_estado']
    search_fields = ['nom_cidade']


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['curriculo']


class InstituicaoEnsinoViewSet(viewsets.ModelViewSet):
    queryset = InstituicaoEnsino.objects.all()
    serializer_class = InstituicaoEnsinoSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormacaoViewSet(viewsets.ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['curriculo']


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['usuario', 'empresa', 'tipo']


class CurriculoViewSet(viewsets.ModelViewSet):
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['usuario']


class StatusInscricaoViewSet(viewsets.ModelViewSet):
    queryset = StatusInscricao.objects.all()
    serializer_class = StatusInscricaoSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusEntrevistaViewSet(viewsets.ModelViewSet):
    queryset = StatusEntrevista.objects.all()
    serializer_class = StatusEntrevistaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntrevistaViewSet(viewsets.ModelViewSet):
    queryset = Entrevista.objects.all()
    serializer_class = EntrevistaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['usuario']


class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['usuario', 'vaga']


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [permissions.IsAuthenticated]
