# Generated by Django 4.2.11 on 2024-06-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_vaccine', '0004_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='country',
            field=models.CharField(default='Russia', max_length=50),
        ),
        migrations.AddField(
            model_name='child',
            name='gender',
            field=models.CharField(default='Boy', max_length=50),
        ),
    ]
