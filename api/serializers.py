from rest_framework import serializers
from api.models import *


class EmpresaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Empresa
    fields = [
      'id', 'cnpj','nome','ramo', 'sede',
    ]


class PaisSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pais
    fields = [
      'id', 'cod_pais', 'sgl_pais', 'nom_pais',
    ]


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = [
            'id', 'cod_estado', 'cod_pais', 'nom_estado', 'sgl_estado'
        ]


class CidadeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cidade
    fields = [
      'id', 'cod_cidade','cod_estado','nom_cidade',
    ]