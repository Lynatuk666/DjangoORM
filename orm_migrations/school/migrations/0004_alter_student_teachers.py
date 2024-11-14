# Generated by Django 5.1.3 on 2024-11-11 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='student', to='school.teacher'),
        ),
    ]
