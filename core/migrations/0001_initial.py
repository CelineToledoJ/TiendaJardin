# Generated by Django 4.2.1 on 2023-06-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]
