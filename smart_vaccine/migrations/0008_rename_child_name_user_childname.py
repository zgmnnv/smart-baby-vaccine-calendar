# Generated by Django 4.2.11 on 2024-06-04 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_vaccine', '0007_alter_user_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='child_name',
            new_name='childname',
        ),
    ]
