# Generated by Django 3.2.16 on 2023-01-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link to read the post', max_length=255),
        ),
    ]
