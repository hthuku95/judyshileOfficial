# Generated by Django 2.2.12 on 2020-08-06 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200806_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='categorys',
        ),
    ]
