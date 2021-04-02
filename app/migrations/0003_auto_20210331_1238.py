# Generated by Django 3.1.7 on 2021-03-31 06:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(150)]),
        ),
    ]
