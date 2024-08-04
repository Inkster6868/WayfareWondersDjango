# Generated by Django 5.0.7 on 2024-08-03 13:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0006_tour_tour_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="tour_id",
            field=models.UUIDField(default=uuid.uuid4,primary_key=True),
        ),
    ]
