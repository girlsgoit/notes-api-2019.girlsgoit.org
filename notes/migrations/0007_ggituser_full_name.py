# Generated by Django 2.2.3 on 2019-07-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20190727_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='ggituser',
            name='full_name',
            field=models.TextField(blank=True),
        ),
    ]