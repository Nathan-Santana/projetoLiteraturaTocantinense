from django.urls import path
from .views import MunicipiosAPIView, EscritoresAPIView, LivrosAPIView, MembrosAPIView, MunicipioAPIView, EscritorAPIView, LivroAPIView, MembroAPIView, EscritorViewSet, MunicipioViewSet, LivroViewSet, MembroViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('municipios', MunicipioViewSet)
router.register(r'escritores', EscritorViewSet)
router.register('livros', LivroViewSet)
router.register('membros', MembroViewSet)

urlpatterns = [
    path('municipios/', MunicipiosAPIView.as_view(), name='municipios'),
    path('municipios/<int:municipio_pk>', MunicipioAPIView.as_view(), name='municipio'),
    path('municipios/<int:municipio_pk>/escritores/', EscritoresAPIView.as_view(), name='municipio_escritores'),
    path('municipios/<int:municipio_pk>/escritores/<int:escritor_pk>', EscritorAPIView.as_view(), name='municipio_escritor'),
    path('escritores/', EscritoresAPIView.as_view(), name='escritores'),
    path('escritores/<int:escritor_pk>', EscritorAPIView.as_view(), name='escritor'),
    path('escritores/<int:escritor_pk>/livros/', EscritorAPIView.as_view(), name='escritor_livros'),
    path('escritores/<int:escritor_pk>/livros/<int:livro_pk>', EscritorAPIView.as_view(), name='escritor_livro'),
    path('livros/', LivrosAPIView.as_view(), name='livros'),
    path('livros/<int:livro_pk>', LivroAPIView.as_view(), name='livro'),
    path('membros/', MembrosAPIView.as_view(), name='membros'),
    path('membros/<int:membro_pk>', MembroAPIView.as_view(), name='membro')
]