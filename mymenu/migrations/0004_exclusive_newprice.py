# Generated by Django 4.0.5 on 2022-08-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymenu', '0003_special_exclusive'),
    ]

    operations = [
        migrations.AddField(
            model_name='exclusive',
            name='newprice',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]