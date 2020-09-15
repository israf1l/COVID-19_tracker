# Generated by Django 3.1 on 2020-08-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorldData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('new', models.CharField(max_length=100)),
                ('active', models.CharField(max_length=100)),
                ('recovered', models.CharField(max_length=100)),
                ('deaths', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
        ),
    ]
