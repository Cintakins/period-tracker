# Generated by Django 4.1.1 on 2022-10-07 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_alter_userprofile_period_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='period_length',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='period_start_date',
        ),
        migrations.CreateModel(
            name='UserPeriodInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start_date', models.DateField(auto_now=True)),
                ('period_length', models.IntegerField(blank=True, default=28, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
