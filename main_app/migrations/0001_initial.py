# Generated by Django 3.2.9 on 2021-12-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=400)),
                ('date', models.DateField(verbose_name='Due Date')),
                ('importance', models.CharField(choices=[('I', 'Important'), ('G', 'General'), ('M', 'Minor')], default='Important', max_length=1)),
            ],
        ),
    ]