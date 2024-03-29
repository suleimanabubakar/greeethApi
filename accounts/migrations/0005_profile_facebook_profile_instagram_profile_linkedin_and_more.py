# Generated by Django 4.0.4 on 2022-09-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_institutionofficial_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tiktok',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(null=True),
        ),
    ]
