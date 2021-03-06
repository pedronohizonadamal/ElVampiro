# Generated by Django 4.0.5 on 2022-06-28 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0004_user_delete_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vampiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=None, max_length=20)),
                ('hab', models.IntegerField(default=None)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('password', models.CharField(default=None, max_length=50)),
                ('bajas', models.IntegerField(default=0)),
                ('bajas_noche', models.IntegerField(default=0)),
                ('victima', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vapp.vampiro')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
