# Generated by Django 2.2.4 on 2020-06-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]