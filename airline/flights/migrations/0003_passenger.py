# Generated by Django 3.2.2 on 2021-05-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20210513_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('flights', models.ManyToManyField(blank=True, related_query_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
