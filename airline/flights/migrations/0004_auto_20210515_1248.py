# Generated by Django 3.2.2 on 2021-05-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
    ]
