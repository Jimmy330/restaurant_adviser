# Generated by Django 2.1.5 on 2020-03-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_adv', '0005_auto_20200307_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.TextField(default='nothing yet'),
        ),
    ]
