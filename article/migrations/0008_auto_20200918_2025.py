# Generated by Django 2.2 on 2020-09-18 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200918_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
