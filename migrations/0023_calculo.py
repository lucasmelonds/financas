# Generated by Django 3.2.3 on 2022-08-31 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0022_receita_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('despesas', models.ManyToManyField(to='financas.Despesa')),
                ('receitas', models.ManyToManyField(to='financas.Receita')),
            ],
        ),
    ]
