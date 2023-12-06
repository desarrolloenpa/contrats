# Generated by Django 5.0 on 2023-12-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Tipo de cliente', max_length=6)),
                ('name', models.CharField(help_text='Nombre de la empresa', max_length=100, unique=True)),
                ('acronym', models.CharField(help_text='Siglas o acronico de la empresa', max_length=100, unique=True)),
                ('first_name', models.CharField(help_text='Nombre del Representante', max_length=50, null=True)),
                ('last_name', models.CharField(help_text='Apellidos del Representante', max_length=50, null=True)),
                ('company_position', models.CharField(help_text='Cargo del Representante', max_length=80, null=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=80, null=True)),
                ('telephone', models.CharField(max_length=80, null=True)),
                ('description', models.TextField(null=True)),
                ('ministry', models.CharField(help_text='Organismo al que pertenece la empresa', max_length=80, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_clients',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Tipo de contrato u orden de trabajo', max_length=3)),
                ('number', models.CharField(help_text='Numero de contrato', max_length=8, unique=True)),
                ('title', models.CharField(help_text='Titulo del contrato', max_length=100)),
                ('value_cup', models.FloatField(help_text='valor CUP de todo los servicios', null=True)),
                ('value_usd', models.FloatField(help_text='valor USD de todo los servicios', null=True)),
                ('date_elaboration', models.DateTimeField(help_text='Fecha de elaboración')),
                ('date_receiving', models.DateTimeField(help_text='Fecha de recibida')),
                ('date_circulation', models.DateTimeField(help_text='Fecha de circulación a las areas')),
                ('date_committed_presentation', models.DateTimeField(help_text='Fecha de circulación al comite')),
                ('date_committed_approved', models.DateTimeField(help_text='Fecha de aprobacion por comite')),
                ('date_client_signature', models.DateTimeField(help_text='Fecha de firma por el cliente')),
                ('date_approved', models.DateTimeField(help_text='Fecha de aprobación')),
                ('date_start', models.DateTimeField(help_text='Fecha de inicio')),
                ('date_end', models.DateTimeField(help_text='Fecha de terminación')),
                ('description', models.TextField(blank=True, help_text='Descripcion del objeto del contrato', null=True)),
                ('observation', models.TextField(blank=True, help_text='Observaciones posibles al contrato en cualquier momento', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_contracts',
            },
        ),
        migrations.CreateModel(
            name='ContractService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('value_cup', models.FloatField(help_text='Valor CUP del servicio en particular', null=True)),
                ('value_usd', models.FloatField(help_text='Valor USD del servicio en particular', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_contract_services',
            },
        ),
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='Estado del contrato', max_length=20, unique=True)),
                ('date_register', models.DateTimeField(help_text='Fecha de tregistro del estado')),
                ('observation', models.TextField(blank=True, help_text='Observaciones posibles al contrato en cualquier momento', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_contract_status',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Numero de la oferta', max_length=8, unique=True)),
                ('value_cup', models.FloatField(help_text='valor CUP de todo los servicios', null=True)),
                ('value_usd', models.FloatField(help_text='valor USD de todo los servicios', null=True)),
                ('observation', models.TextField(blank=True, help_text='Observaciones a la oferta', null=True)),
                ('date_elaboration', models.DateTimeField(help_text='Fecha de elaboración')),
                ('date_client_receiving', models.DateTimeField(help_text='Fecha de recibida por el cliente')),
                ('date_approved', models.DateTimeField(help_text='Fecha de aprobación por el cliente')),
                ('date_receiving', models.DateTimeField(help_text='Fecha de entrega al especialista comercial')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_offers',
            },
        ),
        migrations.CreateModel(
            name='OfferStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='Estado del contrato', max_length=20, unique=True)),
                ('date_register', models.DateTimeField(help_text='Fecha de tregistro del estado')),
                ('observation', models.TextField(blank=True, help_text='Observaciones posibles al contrato en cualquier momento', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_offer_status',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='Numero de la orden', max_length=8, unique=True)),
                ('description', models.TextField(null=True)),
                ('date_elaboration', models.DateTimeField(help_text='Fecha de elaboración')),
                ('date_receiving', models.DateTimeField(help_text='Fecha de recibida')),
                ('date_approved', models.DateTimeField(help_text='Fecha  de cierre de la orden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_orders',
            },
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Descripcion rapida del servicio', max_length=100, unique=True)),
                ('number', models.CharField(max_length=8, unique=True)),
                ('first_name', models.CharField(help_text='Nombre del Solicitante', max_length=50, null=True)),
                ('last_name', models.CharField(help_text='Apellidos del Solicitante', max_length=50, null=True)),
                ('company_position', models.CharField(help_text='Cargo del Solicitante', max_length=80, null=True)),
                ('email', models.EmailField(max_length=80, null=True)),
                ('telephone', models.CharField(max_length=80, null=True)),
                ('description', models.TextField(null=True)),
                ('date_receiving', models.DateTimeField()),
                ('date_approved', models.DateTimeField(null=True)),
                ('date_assigned', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tb_servicies',
            },
        ),
    ]
