# Generated by Django 3.2.8 on 2021-10-19 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0017_remove_flavour_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flavour',
            old_name='ProductN',
            new_name='Product_id',
        ),
    ]
