# Generated by Django 3.2.8 on 2021-10-18 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0012_flavour'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavour',
            name='Ingredientes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='flavour',
            name='Validade',
            field=models.TextField(blank=True),
        ),
    ]
