# Generated by Django 2.1 on 2018-08-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionlink',
            name='answer',
            field=models.CharField(blank=True, default='', max_length=2048),
        ),
    ]