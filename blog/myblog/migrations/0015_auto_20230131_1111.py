# Generated by Django 3.2.16 on 2023-01-31 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
