# Generated by Django 4.0.1 on 2022-02-01 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
