# Generated by Django 3.1.7 on 2021-02-28 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210228_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='user',
        ),
    ]
