# Generated by Django 3.2.9 on 2021-12-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_importance_levels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='importance',
            field=models.CharField(choices=[('I', 'Important'), ('G', 'General'), ('M', 'Minor')], default='G', max_length=1),
        ),
    ]