# Generated by Django 4.2.7 on 2024-02-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_reservation_prix'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default_user.jfif', null=True, upload_to='images/'),
        ),
    ]
