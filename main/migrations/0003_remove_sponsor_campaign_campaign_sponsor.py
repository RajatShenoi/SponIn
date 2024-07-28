# Generated by Django 5.0.7 on 2024-07-28 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_sponsor_campaign"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sponsor",
            name="campaign",
        ),
        migrations.AddField(
            model_name="campaign",
            name="sponsor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.sponsor",
            ),
            preserve_default=False,
        ),
    ]
