# Generated by Django 4.0.4 on 2022-09-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0035_alter_activatetoken_token_alter_resettoken_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activatetoken',
            name='token',
            field=models.PositiveIntegerField(default=135091),
        ),
        migrations.AlterField(
            model_name='resettoken',
            name='token',
            field=models.PositiveIntegerField(default=699444),
        ),
    ]
