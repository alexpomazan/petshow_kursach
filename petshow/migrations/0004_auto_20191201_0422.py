# Generated by Django 2.1.14 on 2019-12-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshow', '0003_auto_20191201_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile-pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
