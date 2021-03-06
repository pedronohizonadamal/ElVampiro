# Generated by Django 4.0.5 on 2022-06-29 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0010_vampiro_bajas_pendientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='BajaRequest',
            fields=[
                ('habitaVamp', models.IntegerField()),
                ('habitaVict', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='vampiro',
            name='victima',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vapp.vampiro'),
        ),
        migrations.CreateModel(
            name='Muerto',
            fields=[
                ('nombre', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('habita', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('bajas', models.IntegerField(default=0)),
                ('bajas_noche', models.IntegerField(default=0)),
                ('bajas_pendientes', models.IntegerField(default=0)),
                ('victima', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vapp.muerto')),
            ],
        ),
    ]
