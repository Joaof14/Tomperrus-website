# Generated by Django 3.2.8 on 2021-10-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0022_auto_20211020_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]
