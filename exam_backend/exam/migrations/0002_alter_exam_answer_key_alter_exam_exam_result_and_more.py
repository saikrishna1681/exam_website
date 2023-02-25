# Generated by Django 4.1.5 on 2023-01-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='answer_key',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_result',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='exam',
            name='marking_scheme',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='question',
            name='statement',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='student_response',
            name='student_response',
            field=models.TextField(blank=True, default=''),
        ),
    ]