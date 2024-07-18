# Generated by Django 5.0.6 on 2024-07-18 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_alter_rental_cant_dias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['fecha']},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='bicicleta',
            new_name='marca',
        ),
        migrations.AddField(
            model_name='cliente',
            name='modelo',
            field=models.CharField(default='modelo', max_length=40),
            preserve_default=False,
        ),
    ]
