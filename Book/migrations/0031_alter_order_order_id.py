# Generated by Django 5.0.1 on 2024-02-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0030_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
