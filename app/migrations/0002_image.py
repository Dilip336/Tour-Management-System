# Generated by Django 3.1.7 on 2021-03-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
