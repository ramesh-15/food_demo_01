# Generated by Django 4.1.5 on 2023-02-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_users_donations_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users_donations",
            name="username",
            field=models.CharField(default=False, max_length=156),
        ),
    ]