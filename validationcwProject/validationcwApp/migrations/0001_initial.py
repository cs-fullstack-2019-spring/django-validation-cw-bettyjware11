# Generated by Django 2.0.6 on 2019-02-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newCarForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='', max_length=200)),
                ('model', models.CharField(default='', max_length=200)),
                ('year', models.IntegerField(default='', max_length=200)),
                ('mpg', models.IntegerField(default='', max_length=200)),
            ],
        ),
    ]
