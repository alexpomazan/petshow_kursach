# Generated by Django 2.1.14 on 2020-02-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshow', '0008_auto_20200223_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(max_length=200, verbose_name='имя автора'),
        ),
    ]
