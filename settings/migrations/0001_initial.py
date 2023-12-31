# Generated by Django 5.0 on 2023-12-05 19:35

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tb_provinces',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.SmallIntegerField(null=True)),
                ('email', models.EmailField(default='desarrollo@local.local', max_length=80, unique=True)),
                ('telephone', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tb_users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='CompanyPosition_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_company_positions',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='company_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.companyposition'),
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='GroupUser_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_groups',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='groupuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CustomUser_groupuser_fk', to='settings.groupuser'),
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipality_province_fk', to='settings.province')),
            ],
            options={
                'db_table': 'tb_municipalities',
            },
        ),
        migrations.CreateModel(
            name='SalaryScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3)),
                ('salary', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='SalaryScale_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_salary_scales',
            },
        ),
        migrations.AddField(
            model_name='companyposition',
            name='salary_scale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.salaryscale'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='salary_scale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.salaryscale'),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value_cup', models.FloatField(help_text='Valor CUP segun la norma', null=True)),
                ('value_usd', models.FloatField(help_text='Valor USD segun la norma', null=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_at', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='service_type_user_fk', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_service_types',
            },
        ),
    ]
