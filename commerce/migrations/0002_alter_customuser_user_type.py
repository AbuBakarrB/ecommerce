# Generated by Django 5.0.6 on 2024-06-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commerce", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("buyer", "Buyer"), ("seller", "Seller")],
                default="buyer",
                max_length=7,
            ),
        ),
    ]
