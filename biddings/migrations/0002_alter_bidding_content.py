# Generated by Django 3.2.16 on 2022-12-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biddings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='content',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
