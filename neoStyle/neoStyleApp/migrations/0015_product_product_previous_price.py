# Generated by Django 4.1.6 on 2023-02-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoStyleApp', '0014_product_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_previous_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]