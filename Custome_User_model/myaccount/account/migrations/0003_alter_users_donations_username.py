# Generated by Django 4.1.5 on 2023-02-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_users_donations_username_alter_users_donations_flag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users_donations",
            name="username",
            field=models.CharField(blank="", max_length=156),
        ),
    ]
