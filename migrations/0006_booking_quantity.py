# Generated by Django 2.2.6 on 2020-03-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_auto_20200324_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='quantity',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
