# Generated by Django 5.0.6 on 2024-07-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0016_remove_cliente_cant_dias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='cant_dias',
            field=models.DateField(),
        ),
    ]
