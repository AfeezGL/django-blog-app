# Generated by Django 2.2 on 2020-05-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
