# Generated by Django 5.0.1 on 2024-02-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('job_time', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=100)),
                ('place_of_work', models.CharField(max_length=100)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
