from django.contrib import admin
from app.models import Especialidade, Medico, Medicamento, Quarto, Paciente, Paciente_Medicacao, HistoricoClinico, Enfermeiro

# Register your models here.
admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Quarto)
admin.site.register(Paciente)
admin.site.register(Paciente_Medicacao)
admin.site.register(HistoricoClinico)
admin.site.register(Enfermeiro)

