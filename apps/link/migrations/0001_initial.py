# Generated by Django 3.1.7 on 2021-03-21 07:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=1024, verbose_name='Link')),
                ('uses', models.IntegerField(default=0, verbose_name='Uses count')),
                ('shortened', models.URLField(default=None, null=True, verbose_name='Shortened link')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]
