# Generated by Django 3.2.8 on 2021-10-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0005_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ImageFile',
            field=models.ImageField(blank=True, upload_to='static/tomperrus'),
        ),
    ]
