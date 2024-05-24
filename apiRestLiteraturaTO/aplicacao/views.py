from django.shortcuts import render
from rest_framework import generics
from .models import Municipio, Escritor, Livro, Membro
from .serializers import MunicipioSerializer, EscritorSerializer, LivroSerializer, MembroSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import EhSuperUser

class MunicipiosAPIView(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class MunicipioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class EscritoresAPIView(generics.ListCreateAPIView):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer

    def get_queryset(self):
        if self.kwargs.get('municipio_pk'):
            return self.queryset.filter(municipio_id = self.kwargs.get('municipio_pk'))
        return self.queryset.all()

class EscritorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer

    def get_object(self):
        if self.kwargs.get('municipio_pk'):
            return get_object_or_404(self.get_queryset(), municipio_id = self.kwargs.get('municipio_pk'), pk=self.kwargs.get('escritor_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('escritor_pk'))


class LivrosAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_queryset(self):
        if self.kwargs.get('escritor_pk'):
            return self.queryset.filter(escritor_id = self.kwargs.get('escritor_pk'))
        return self.queryset.all()

class LivroAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_object(self):
        if self.kwargs.get('escritor_pk'):
            return get_object_or_404(self.get_queryset(), escritor_id = self.kwargs.get('escritor_pk'), pk=self.kwargs.get('livro_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('livro_pk'))    


class MembrosAPIView(generics.ListCreateAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class MembroAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['get'])
    def escritores(self, request, pk=None):
        
        self.pagination_class.page_size = 1
        escritores = Escritor.objects.filter(Municipio_id = pk)
        page = self.paginate_queryset(escritores)

        if page is not None:
            serializer = EscritorSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EscritorSerializer(escritores.all(), many=True)
        return Response(serializer.data)

class EscritorViewSet(viewsets.ModelViewSet):
    queryset = Escritor.objects.all()
    serializer_class = EscritorSerializer

    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['get'])
    def livros(self, request, pk=None):
        
        self.pagination_class.page_size = 1
        livros = Livro.objects.filter(autor_id = pk)
        page = self.paginate_queryset(livros)

        if page is not None:
            serializer = LivroSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EscritorSerializer(livros.all(), many=True)
        return Response(serializer.data)
    
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions,)

class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions,)    

