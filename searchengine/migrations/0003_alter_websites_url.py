# Generated by Django 5.0.4 on 2024-04-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0002_delete_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='url',
            field=models.URLField(db_index=True),
        ),
    ]