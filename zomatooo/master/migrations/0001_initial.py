# Generated by Django 5.0.6 on 2024-06-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_desc', models.CharField(max_length=50)),
                ('item_type', models.CharField(choices=[('veg', 'veg'), ('Non-Veg', 'Non-Veg'), ('egg', 'egg')], max_length=50)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
