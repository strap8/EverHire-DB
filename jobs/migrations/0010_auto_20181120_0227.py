# Generated by Django 2.1.1 on 2018-11-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20181120_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
    ]