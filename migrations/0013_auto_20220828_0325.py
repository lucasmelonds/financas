# Generated by Django 3.2.3 on 2022-08-28 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0012_auto_20220828_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balanco',
            name='despesas',
        ),
        migrations.AddField(
            model_name='balanco',
            name='despesas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='financas.despesa'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='balanco',
            name='receitas',
        ),
        migrations.AddField(
            model_name='balanco',
            name='receitas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='financas.receita'),
            preserve_default=False,
        ),
    ]
