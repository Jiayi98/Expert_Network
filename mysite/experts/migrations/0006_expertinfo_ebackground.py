# Generated by Django 2.2.1 on 2019-07-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0005_auto_20190704_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertinfo',
            name='ebackground',
            field=models.TextField(blank=True),
        ),
    ]
