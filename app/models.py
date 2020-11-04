from django.db import models

# Create your models here.
# se usar esta classe nas classes derivadas colocar como argumento Pessoa inves de models.Model
# class Pessoa(models.Model):
#     nome = models.CharField(max_length=70)
#     cc = models.IntegerField()
#     genero = models.CharField()

class Medico(models.Model):
    nome=models.CharField(max_length=70)
    nmec=models.IntegerField()
    cc=models.IntegerField()
    especialidade=models.CharField(max_length=40)
    gabinte=models.IntegerField()
    # duvida: como modelar um horario
    def __str__(self):
        return self.name

class HistoricoClinico(models.Model):# falta acabar
    data=models.DateField()

class Medicamento(models.Model):
    nome=models.CharField(max_length=30)
    laboratorio=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Paciente(models.Model):
    nome=models.CharField(max_length=70)
    cc = models.IntegerField()
    nif=models.IntegerField()
    n_utente=models.IntegerField()
    dataNasc=models.DateField()
    genero=models.CharField()
    quarto=models.IntegerField()
    medico=models.ForeignKey(Medico)
    def __str__(self):
        return self.name

class Paciente_Medicacao(models.Model):#normalização
    paciente=models.ForeignKey(Paciente)
    medicamento=models.ForeignKey(Medicamento)

