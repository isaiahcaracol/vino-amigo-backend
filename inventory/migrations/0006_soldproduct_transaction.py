# Generated by Django 4.0.4 on 2022-08-28 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_soldproduct_transaction_delete_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldproduct',
            name='transaction',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='inventory.transaction'),
            preserve_default=False,
        ),
    ]