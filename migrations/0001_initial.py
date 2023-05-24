# Generated by Django 3.2.3 on 2022-08-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balanco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('data_pub', models.DateTimeField(verbose_name='Data de Publicação')),
                ('data_fim', models.DateField(null=True, verbose_name='Data de Encerramento')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('data_pub', models.DateTimeField(verbose_name='Data de Publicação')),
                ('data_fim', models.DateField(null=True, verbose_name='Data de Encerramento')),
            ],
        ),
    ]
