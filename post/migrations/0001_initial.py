# Generated by Django 3.2.4 on 2021-06-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.CharField(max_length=100)),
                ('image1', models.ImageField(default='defo', upload_to='documents/')),
                ('image2', models.ImageField(blank=True, default='defo', upload_to='documents/')),
                ('image3', models.ImageField(blank=True, default='defo', upload_to='documents/')),
                ('image4', models.ImageField(blank=True, default='defo', upload_to='documents/')),
                ('image5', models.ImageField(blank=True, default='defo', upload_to='documents/')),
                ('description', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
