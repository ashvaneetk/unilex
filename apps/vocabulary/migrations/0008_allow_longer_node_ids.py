# Generated by Django 2.0.8 on 2018-09-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0007_vocabulary_force_unique_nodeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='node_id',
            field=models.SlugField(blank=True, max_length=127, verbose_name='Permalink ID'),
        ),
    ]