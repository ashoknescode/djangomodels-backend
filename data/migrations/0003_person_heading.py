# Generated by Django 2.1.4 on 2019-01-05 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20190105_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='heading',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
