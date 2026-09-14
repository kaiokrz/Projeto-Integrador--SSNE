from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser

class Curso(models.TextChoices):
    INFO = 'INFO', 'Informática'
    EDIFIC = 'EDIFIC', 'Edificações'
    MAMB = 'MAMB', 'Meio Ambiente'
    OUTRO = 'OUTRO', 'Outro'


class User(AbstractUser):
    curso = models.CharField(
        max_length=10,
        choices=Curso.choices,
        blank=True,
        null=True,
        verbose_name="Curso",
    )

    def __str__(self):
        return self.username


class Bloco(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="blocos", blank=True, null=True)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    class Categoria(models.TextChoices):
        SALA_AULA = 'SALA', 'Sala de aula'
        SECRETARIA = 'SECRE', 'Secretaria'
        COORDENACAO = 'COORD', 'Coordenação'
        LABORATORIO = 'LAB', 'Laboratório'
        BIBLIOTECA = 'BIBLIO', 'Biblioteca'
        CANTINA = 'CANT', 'Cantina/Refeitório'
        OUTRO = 'OUTRO', 'Outro'

    nome = models.CharField(max_length=100)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE, related_name="setores")
    categoria = models.CharField(max_length=10, choices=Categoria.choices, default=Categoria.OUTRO)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.bloco.nome})"


class Aviso(models.Model):
    titulo = models.CharField(max_length=150)
    curso = models.CharField(
        max_length=10,
        choices=Curso.choices,
        blank=True,
        null=True,
        help_text="Deixe em branco para exibir o aviso para todos os cursos.",
    )
    imagem = models.ImageField(upload_to="avisos", blank=True, null=True)
    conteudo = HTMLField()
    data_publicacao = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo


class Mensagem(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email