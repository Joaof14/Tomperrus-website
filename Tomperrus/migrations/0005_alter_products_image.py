# Generated by Django 3.2.8 on 2021-10-16 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0004_auto_20211016_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.CharField(max_length=64),
        ),
    ]
