# Generated by Django 4.0.4 on 2022-09-09 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_set', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_companies', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutions', to='accounts.institutioncategories')),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionOfficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_on', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officials', to='accounts.institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'institution')},
            },
        ),
    ]
