# Generated by Django 4.0.4 on 2022-07-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_profile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_image',
            field=models.ImageField(default='Test2_pZeWKsl.png', upload_to='profile_image'),
        ),
    ]