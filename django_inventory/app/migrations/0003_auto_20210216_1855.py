# Generated by Django 3.1.5 on 2021-02-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210215_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='date_bought',
        ),
        migrations.AddField(
            model_name='games',
            name='how_much_liked',
            field=models.CharField(choices=[('Liked', 'Liked'), ('OK', 'OK'), ('Not Liked', 'Not Liked')], max_length=20, null=True),
        ),
    ]
