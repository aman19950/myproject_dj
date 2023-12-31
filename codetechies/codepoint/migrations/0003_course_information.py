# Generated by Django 3.1.4 on 2023-11-07 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codepoint', '0002_auto_20231107_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('course_cat_id', models.CharField(max_length=100, null=True)),
                ('s_no', models.IntegerField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='codepoint.course_category')),
            ],
        ),
    ]
