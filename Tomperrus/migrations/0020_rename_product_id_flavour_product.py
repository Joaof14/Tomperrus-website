# Generated by Django 3.2.8 on 2021-10-19 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tomperrus', '0019_rename_product_id_flavour_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flavour',
            old_name='product_id',
            new_name='product',
        ),
    ]
