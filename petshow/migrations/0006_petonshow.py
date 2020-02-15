# Generated by Django 2.1.14 on 2020-02-14 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petshow', '0005_auto_20191210_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetOnShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], default='male', max_length=50)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pets_pics')),
                ('info', models.TextField(blank=True)),
                ('show', models.CharField(blank=True, choices=[('dogs', 'dogs'), ('cats', 'cats')], default=None, max_length=10, null=True)),
                ('can_vote_before_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('likes', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
