# Generated by Django 3.1.5 on 2021-03-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyplan',
            name='name',
            field=models.CharField(max_length=35, null=True),
        ),
    ]