# Generated by Django 3.2.4 on 2021-07-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20210703_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, default='/default', null=True, upload_to='documents/'),
        ),
    ]
