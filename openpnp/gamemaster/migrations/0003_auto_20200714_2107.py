# Generated by Django 3.0.6 on 2020-07-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamemaster', '0002_auto_20200713_0344'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Template',
            new_name='TemplateModel',
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('min_value', models.IntegerField(default=0)),
                ('max_value', models.IntegerField(default=100)),
                ('related_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamemaster.TemplateModel')),
            ],
        ),
    ]
