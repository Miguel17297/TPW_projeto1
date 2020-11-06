# Generated by Django 3.1.3 on 2020-11-05 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('laboratorio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmec', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('cc', models.IntegerField()),
                ('especialidade', models.CharField(max_length=40)),
                ('gabinte', models.IntegerField()),
                ('ncedulaprofissional', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('cc', models.IntegerField()),
                ('nif', models.IntegerField()),
                ('n_utente', models.IntegerField()),
                ('dataNasc', models.DateField()),
                ('genero', models.CharField(max_length=2)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('limite', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_Medicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo_de_medicacao', models.CharField(max_length=200)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicamento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='quarto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quarto'),
        ),
        migrations.CreateModel(
            name='HistoricoClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('anotacao', models.CharField(max_length=500)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmec', models.IntegerField()),
                ('nome', models.CharField(max_length=70)),
                ('cc', models.IntegerField()),
                ('ncedulaprofissional', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('quarto', models.ManyToManyField(to='app.Quarto')),
            ],
        ),
    ]