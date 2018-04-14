# Generated by Django 2.0.2 on 2018-03-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0006_auto_20180325_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'ToDo',
                'verbose_name_plural': 'ToDo',
            },
        ),
    ]