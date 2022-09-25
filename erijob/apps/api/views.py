# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from knox.views import LoginView as KnoxLoginView

from erijob.apps.api.models import Empresa, Estado, Cidade, Curriculo, InstituicaoEnsino, Formacao, StatusInscricao, \
    StatusEntrevista, Experiencia, Inscricao, Vaga, Usuario, Pais
from erijob.apps.api.serializers import EmpresaSerializer, EstadoSerializer, CidadeSerializer, \
    CurriculoSerializer, InstituicaoEnsinoSerializer, FormacaoSerializer, StatusInscricaoSerializer, \
    StatusEntrevistaSerializer, ExperienciaSerializer, InscricaoSerializer, VagaSerializer, UsuarioSerializer, \
    GroupSerializer, PaisSerializer, UsuarioCadastroSerializer


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

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [permissions.IsAuthenticated]


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['cod_estado', 'nom_cidade']


class ExperienciaViewSet(viewsets.ModelViewSet):
    queryset = Experiencia.objects.all()
    serializer_class = ExperienciaSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstituicaoEnsinoViewSet(viewsets.ModelViewSet):
    queryset = InstituicaoEnsino.objects.all()
    serializer_class = InstituicaoEnsinoSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormacaoViewSet(viewsets.ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurriculoViewSet(viewsets.ModelViewSet):
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusInscricaoViewSet(viewsets.ModelViewSet):
    queryset = StatusInscricao.objects.all()
    serializer_class = StatusInscricaoSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatusEntrevistaViewSet(viewsets.ModelViewSet):
    queryset = StatusEntrevista.objects.all()
    serializer_class = StatusEntrevistaSerializer
    permission_classes = [permissions.IsAuthenticated]


class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    permission_classes = [permissions.IsAuthenticated]


class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [permissions.IsAuthenticated]
