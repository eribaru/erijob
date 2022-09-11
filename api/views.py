# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from api.models import Empresa, Estado, Cidade, Curriculo, InstituicaoEnsino, Formacao, StatusInscricao, \
    StatusEntrevista, Experiencia, Inscricao, Vaga, Usuario
from api.serializers import EmpresaSerializer, EstadoSerializer, CidadeSerializer, \
    CurriculoSerializer, InstituicaoEnsinoSerializer, FormacaoSerializer, StatusInscricaoSerializer, \
    StatusEntrevistaSerializer, ExperienciaSerializer, InscricaoSerializer, VagaSerializer, UsuarioSerializer, \
    UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
    permission_classes = [permissions.IsAuthenticated]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [permissions.IsAuthenticated]


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