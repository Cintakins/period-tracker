# Generated by Django 4.1.1 on 2022-10-08 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_userprofile_period_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperiodinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]