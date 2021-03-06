# Generated by Django 2.1.4 on 2019-01-06 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
