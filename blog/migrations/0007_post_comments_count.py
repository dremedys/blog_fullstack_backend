# Generated by Django 3.2 on 2021-05-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
