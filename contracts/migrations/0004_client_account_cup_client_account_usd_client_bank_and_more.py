# Generated by Django 5.0 on 2023-12-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_alter_client_ministry'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='account_cup',
            field=models.CharField(help_text='Cuenta CUP', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='account_usd',
            field=models.CharField(help_text='Cuenta USD', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='bank',
            field=models.CharField(help_text='Datos de Banco', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='bank_branch',
            field=models.CharField(help_text='Datos de Sucursal bancaria', max_length=80, null=True),
        ),
    ]
