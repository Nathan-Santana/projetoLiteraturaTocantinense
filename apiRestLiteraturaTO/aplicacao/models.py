from django.db import models

class Base(models.Model):
    class Meta:
        abstract = True

class Municipio(Base):
    nome = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ['id']
    
    def __str__(self):
        return self.nome            

class Escritor(Base):
    nome = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, related_name='escritores', on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, default='')
    
    class Meta:
        verbose_name = 'Escritor'
        verbose_name_plural = 'Escritores'
        ordering = ['id']

    def __str__(self):
        return self.nome


class Membro(Base):  
    nome = models.CharField(max_length=255) 
    funcao = models.TextField(blank=True, default='')
    lattes = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['id']    

    def __str__(self):
        return self.nome    

class Livro(Base):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, default='')
    link = models.URLField(unique=True)
    autor = models.ForeignKey(Escritor, related_name='livros', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        unique_together = ['titulo', 'autor']
        ordering = ['id']

    def __str__(self):
        return f'{self.titulo}, escrito por {self.autor}.'        
