# Generated by Django 3.2.8 on 2021-11-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0036_auto_20211101_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image1',
            field=models.CharField(blank=True, default='media/images/NOME DO ARQUIVO', max_length=64),
        ),
    ]
