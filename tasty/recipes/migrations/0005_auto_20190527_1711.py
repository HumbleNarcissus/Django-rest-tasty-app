# Generated by Django 2.2.1 on 2019-05-27 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190527_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='author',
            new_name='owner',
        ),
    ]