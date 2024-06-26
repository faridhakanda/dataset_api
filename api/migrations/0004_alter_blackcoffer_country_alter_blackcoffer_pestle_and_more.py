# Generated by Django 5.0.6 on 2024-06-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blackcoffer_end_year_alter_blackcoffer_insight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackcoffer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blackcoffer',
            name='pestle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blackcoffer',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blackcoffer',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blackcoffer',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blackcoffer',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
