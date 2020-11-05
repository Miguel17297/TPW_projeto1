from django.db import models


# Create your models here.

class Medico(models.Model):
    nmec = models.IntegerField()
    nome = models.CharField(max_length=70)
    cc = models.IntegerField()
    especialidade = models.CharField(max_length=40)
    gabinte = models.IntegerField()
    ncedulaprofissional = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=40)  # Validar Password

    # Horário

    # Pacientes # Existem vários pacientes para cada médico
    def __str__(self):
        return self.name


class Medicamento(models.Model):
    nome = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Quarto(models.Model):
    numero = models.IntegerField()
    limite = models.IntegerField()


class Paciente(models.Model):
    nome = models.CharField(max_length=70)
    cc = models.IntegerField()
    nif = models.IntegerField()
    n_utente = models.IntegerField()
    dataNasc = models.DateField()
    genero = models.CharField(max_length=2) # M, F, ou NS
    # quarto = models.IntegerField()
    ## Um paciente apenas está em 1 quarto mas 1 quarto tem vários pacientes
    quarto = models.ForeignKey(Quarto,
                               on_delete=models.CASCADE)
    ## Existem vários pacientes para cada médico mas cada paciente apenas tem 1 médico
    medico = models.ForeignKey(Medico,
                               on_delete=models.CASCADE)

    # medicacao = models.ManyToManyField(Medicamento)  # Cada paciente toma vários medicamentos e o mesmo medicamento pode ser tomado por vários pacientes
    # Histórico Clínico # Para um dia específico e por paciente


    def __str__(self):
        return self.name


class Paciente_Medicacao(models.Model): # normalização
    paciente=models.ForeignKey(Paciente,
                               on_delete=models.CASCADE)
    medicamento=models.ForeignKey(Medicamento,
                               on_delete=models.CASCADE)
    modo_de_medicacao=models.CharField(max_length=200)  # A ser escrito pelo médico para cada paciente específico


class HistoricoClinico(models.Model):
    paciente = models.ForeignKey(Paciente,
                               on_delete=models.CASCADE)
    data=models.DateField()
    anotacao = models.CharField(max_length=500) # A ser escrito pelo médico para cada paciente específico


class Enfermeiro(models.Model):
    nmec = models.IntegerField()
    nome = models.CharField(max_length=70)
    cc = models.IntegerField()
    ncedulaprofissional = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=40)  # Validar Password
    ## Um quarto tem vários enfermeiros e um enfermeiro está responsável por mais de 1 quarto
    quarto = models.ManyToManyField(Quarto)

    ## Horário




# se usar esta classe nas classes derivadas colocar como argumento Pessoa inves de models.Model
# class Pessoa(models.Model):
#     nome = models.CharField(max_length=70)
#     cc = models.IntegerField()
#     genero = models.CharField()
#
# class Medico(models.Model):
#     nome=models.CharField(max_length=70)
#     nmec=models.IntegerField()
#     cc=models.IntegerField()
#     especialidade=models.CharField(max_length=40)
#     gabinte=models.IntegerField()
#     # duvida: como modelar um horario
#     def __str__(self):
#         return self.name
#
# class HistoricoClinico(models.Model):# falta acabar
#     data=models.DateField()
#
# class Medicamento(models.Model):
#     nome=models.CharField(max_length=30)
#     laboratorio=models.CharField(max_length=50)
#     def __str__(self):
#         return self.name
#
# class Paciente(models.Model):
#     nome=models.CharField(max_length=70)
#     cc = models.IntegerField()
#     nif=models.IntegerField()
#     n_utente=models.IntegerField()
#     dataNasc=models.DateField()
#     genero=models.CharField()
#     quarto=models.IntegerField()
#     medico=models.ForeignKey(Medico)
#     def __str__(self):
#         return self.name
#
# class Paciente_Medicacao(models.Model):#normalização
#     paciente=models.ForeignKey(Paciente)
#     medicamento=models.ForeignKey(Medicamento)
