from rest_framework import serializers
from .models import Municipio, Escritor, Membro, Livro
import logging

logger = logging.getLogger(__name__)

class MunicipioNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = (
            'id',
            'nome',
        )

class EscritorSerializer(serializers.ModelSerializer):
    municipio = serializers.PrimaryKeyRelatedField(queryset=Municipio.objects.all())
    class Meta:
        model = Escritor
        fields = (
            'id',
            'nome',
            'municipio',
            'descricao',
        )


class LivroSerializer(serializers.ModelSerializer):
    autor = serializers.PrimaryKeyRelatedField(queryset=Escritor.objects.all())

    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'descricao',
            'link',
            'autor'
        )


class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = (
            'id',
            'nome',
            'funcao',
            'lattes',
        )