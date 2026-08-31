from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    datare = models.DateField(auto_now=True)
    dataev = models.DateField()
    local = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

class Aluno(models.Model):
    class Curso(models.TextChoices):
        info = 'INFO', 'Informática'
        mamb = 'MAMB', 'Meio Ambiente'
        edific = 'EDIFIC', 'Edificacoes'
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    curso = models.CharField(max_length=15, choices=Curso.choices)
    ano = models.IntegerField
