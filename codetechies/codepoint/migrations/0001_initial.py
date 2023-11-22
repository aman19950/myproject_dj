# Generated by Django 3.1.4 on 2023-11-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
