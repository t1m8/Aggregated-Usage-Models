# Generated by Django 2.2.1 on 2021-08-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usage', '0007_auto_20210810_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bothusagerecord',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
