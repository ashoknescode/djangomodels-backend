# Generated by Django 2.1.4 on 2019-01-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20190106_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='about',
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
