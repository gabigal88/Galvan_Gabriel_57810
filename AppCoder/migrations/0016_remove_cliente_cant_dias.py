# Generated by Django 5.0.6 on 2024-07-16 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_alter_cliente_cant_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cant_dias',
        ),
    ]
