# Generated by Django 5.0.1 on 2024-01-09 14:02

import bet.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('condicao', models.CharField(max_length=400)),
                ('apostaMax', models.FloatField()),
                ('multiplicador', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('statusBet', models.IntegerField(choices=[(bet.models.StatusBet['AGUARDANDO_PAGAMENTO'], 0), (bet.models.StatusBet['APOSTADO'], 1), (bet.models.StatusBet['VITORIA'], 2), (bet.models.StatusBet['DERROTA'], 3), (bet.models.StatusBet['EXPIRADA'], 4)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userBet', to='user.user')),
                ('betType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betType', to='bet.bettype')),
            ],
        ),
        migrations.AddField(
            model_name='bettype',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='bet.game'),
        ),
    ]
