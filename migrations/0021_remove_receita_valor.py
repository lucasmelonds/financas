# Generated by Django 3.2.3 on 2022-08-31 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0020_auto_20220831_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='valor',
        ),
    ]
