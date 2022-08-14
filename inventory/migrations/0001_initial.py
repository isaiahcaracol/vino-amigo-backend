# Generated by Django 4.0.4 on 2022-05-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('barcode', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('net_weight', models.TextField(max_length=255)),
                ('flavor', models.TextField(max_length=255)),
                ('alcohol_content', models.TextField(max_length=255)),
                ('current_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]