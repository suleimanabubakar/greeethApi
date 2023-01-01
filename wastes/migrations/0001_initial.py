# Generated by Django 4.0.4 on 2023-01-01 08:01

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RecycleWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('location', django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_recycled', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WasteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WasteBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_bids', to=settings.AUTH_USER_MODEL)),
                ('waste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='wastes.recyclewaste')),
            ],
        ),
        migrations.CreateModel(
            name='SoldWaste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=40)),
                ('transacted_on', models.DateTimeField(auto_now_add=True)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_bids', to='wastes.wastebid')),
                ('waste', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sold_waste', to='wastes.recyclewaste')),
            ],
        ),
        migrations.AddField(
            model_name='recyclewaste',
            name='waste_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recycled_waste', to='wastes.wastetype'),
        ),
    ]