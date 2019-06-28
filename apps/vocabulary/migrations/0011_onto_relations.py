# Generated by Django 2.2.1 on 2019-06-23 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0010_authority_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_value_type', models.CharField(blank=True, choices=[
                    ('char', 'One or more characters'),
                    ('bool', 'Yes or No'),
                    ('json', 'Valid JSON'),
                    ('int', 'Integer number'),
                    ('dec', 'Decimal number')], max_length=4, null=True, verbose_name='Object type')),
                ('object_value', models.TextField(blank=True, null=True, verbose_name='Object value')),
            ],
            options={
                'verbose_name': 'Concept Relation',
                'verbose_name_plural': 'Concept Relations',
                'db_table': 'concept_relations',
            },
        ),
        migrations.RemoveField(
            model_name='conceptattribute',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='conceptattribute',
            name='option',
        ),
        migrations.AlterUniqueTogether(
            name='synonym',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='synonym',
            name='concept',
        ),
        migrations.RemoveField(
            model_name='concept',
            name='related'
        ),
        migrations.AddField(
            model_name='concept',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='relations',
                                         through='vocabulary.Relation', to='vocabulary.Concept'),
        ),
        migrations.DeleteModel(
            name='AttributeOption',
        ),
        migrations.DeleteModel(
            name='ConceptAttribute',
        ),
        migrations.DeleteModel(
            name='Synonym',
        ),
        migrations.AddField(
            model_name='relation',
            name='object',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='object', to='vocabulary.Concept'),
        ),
        migrations.AddField(
            model_name='relation',
            name='predicate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='predicate', to='vocabulary.Concept'),
        ),
        migrations.AddField(
            model_name='relation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='subject', to='vocabulary.Concept'),
        ),
    ]