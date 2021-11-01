# Generated by Django 3.2.8 on 2021-10-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0003_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='static/tomperrus'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.FloatField(),
        ),
    ]
