# Generated by Django 3.0.3 on 2020-02-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]