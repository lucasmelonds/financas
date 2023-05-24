# Generated by Django 3.2.3 on 2022-09-01 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0029_auto_20220901_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalancoNome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='despesa',
            name='valor',
            field=models.IntegerField(null=True, verbose_name='Despesa mensal'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='valor',
            field=models.IntegerField(null=True, verbose_name='Receita mensal'),
        ),
        migrations.AddField(
            model_name='balanco',
            name='balanconome',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='financas.balanconome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='despesa',
            name='balanconome',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='financas.balanconome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receita',
            name='balanconome',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='financas.balanconome'),
            preserve_default=False,
        ),
    ]
