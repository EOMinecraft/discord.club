# Generated by Django 2.1 on 2019-02-20 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190220_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='label',
        ),
    ]