# Generated by Django 2.2.1 on 2019-05-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default='xyz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
