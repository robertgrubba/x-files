# Generated by Django 4.0.1 on 2022-02-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_remove_person_notes_remove_person_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='url',
            field=models.URLField(),
        ),
    ]
