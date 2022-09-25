from django.contrib.auth.models import Group
from rest_framework import serializers
from erijob.apps.api.models import *


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UsuarioSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:usuario-detail")

    class Meta:
        model = Usuario
        fields = [
            'url', 'email', 'date_of_birth', 'telefone', 'password', 'tipo', 'cpf'
        ]


class UsuarioCadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'password', 'email', 'nome','cpf','date_of_birth', 'tipo')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = Usuario.objects.create(
            email=validated_data['email'],
            nome=validated_data['nome'],
            cpf=validated_data['cpf'],
            date_of_birth=validated_data['date_of_birth'],
            tipo=validated_data['tipo']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            'id', 'cnpj', 'nome', 'ramo', 'sede',
        ]


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = [
            'cod_pais', 'sgl_pais', 'nom_pais',
        ]


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = [
             'cod_estado', 'cod_pais', 'nom_estado', 'sgl_estado'
        ]


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = [
             'cod_cidade', 'cod_estado', 'nom_cidade',
        ]


class ExperienciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiencia
        fields = [
            'id', 'area', 'cargo', 'local', 'inicio', 'fim', 'atual', 'empresa', 'curriculo'
        ]


class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = [
            'id', 'objetivo', 'contato', 'dados_pessoais', 'sobre', 'usuario',
        ]


class InstituicaoEnsinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoEnsino
        fields = [
            'id', 'nome', 'sede',
        ]


class FormacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formacao
        fields = [
            'id', 'area', 'nivel', 'inicio', 'previsao_termino', 'em_andamento', 'instituicao', 'curriculo',
        ]


class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEntrevista
        fields = [
            'id', 'valor',
        ]


class StatusInscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusInscricao
        fields = [
            'id', 'valor',
        ]


class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = [
            'id', 'feedback', 'data_inscricao', 'apto_entrevista', 'vaga', 'feedback', 'usuario', 'status',
        ]


class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevista
        fields = [
            'id', 'feedback', 'data', 'status', 'inscricao'
        ]


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [
            'id', 'area', 'cargo', 'resposabilidades', 'requisitos', 'pcsc', 'remoto', 'local', 'cargo_horaria',
            'data_cadastro', 'data_fechamento', 'tipo_contrato', 'contratacao', 'empresa',
        ]
