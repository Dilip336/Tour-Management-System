# Generated by Django 3.1.7 on 2021-03-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]
