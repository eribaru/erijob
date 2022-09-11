from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, permissions

from api.models import Empresa
from api.serializers import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
