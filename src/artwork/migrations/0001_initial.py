# Generated by Django 3.0.6 on 2020-05-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image_url', models.CharField(max_length=350)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]