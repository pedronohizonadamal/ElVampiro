# Generated by Django 4.0.5 on 2022-06-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('habitacion', models.IntegerField()),
                ('bajas', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
