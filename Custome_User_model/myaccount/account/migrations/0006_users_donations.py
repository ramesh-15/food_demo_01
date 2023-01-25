# Generated by Django 4.1.5 on 2023-01-25 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_doner_details_ngo_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users_donations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ud_username",
                    models.CharField(max_length=100, verbose_name="User Name"),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("donar_contact", models.IntegerField()),
                (
                    "food_type",
                    models.CharField(
                        choices=[("1", "VEG"), ("2", "NON-VEG")], max_length=100
                    ),
                ),
                ("food_items", models.CharField(max_length=200)),
                ("quantity", models.PositiveIntegerField()),
                ("food_pick_up", models.CharField(max_length=200)),
                ("pincode", models.PositiveIntegerField()),
                (
                    "donation",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.doner_details",
                    ),
                ),
            ],
        ),
    ]
