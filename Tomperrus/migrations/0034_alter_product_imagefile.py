# Generated by Django 3.2.8 on 2021-11-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0033_alter_product_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ImageFile',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
