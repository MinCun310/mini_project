# Generated by Django 4.2.4 on 2024-03-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvdata',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='csvdata',
            name='start_date',
            field=models.DateField(),
        ),
    ]
