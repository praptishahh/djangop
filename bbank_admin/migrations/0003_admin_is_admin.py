# Generated by Django 3.2.7 on 2021-12-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbank_admin', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='is_admin',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]