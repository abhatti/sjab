# Generated by Django 2.0.6 on 2018-08-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_voucher_voucheritemmapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucher',
            name='voucher_number',
            field=models.BigIntegerField(auto_created=True, blank=True, null=True, unique=True),
        ),
    ]