# Generated by Django 4.2.7 on 2024-02-05 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_merge_0003_message_0004_offre_capacite_offre_lieu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
    ]
