# Generated by Django 3.0.6 on 2020-07-14 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamemaster', '0009_auto_20200715_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatemodel',
            name='attributes',
            field=models.ManyToManyField(to='gamemaster.AttributeTemplateModel'),
        ),
    ]