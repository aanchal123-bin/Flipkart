# Generated by Django 4.2.1 on 2023-06-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customeraddress_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='pin_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='street_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
