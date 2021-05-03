# Generated by Django 3.2 on 2021-04-19 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('humidity', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='datapoints',
        ),
        migrations.DeleteModel(
            name='Datapoints',
        ),
        migrations.AddField(
            model_name='datapoint',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location'),
        ),
    ]
