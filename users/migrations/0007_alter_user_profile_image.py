# Generated by Django 4.0.4 on 2022-07-05 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(blank=True, default='Test2.png', max_length=200, null=True, upload_to='profile_image/'),
        ),
    ]
