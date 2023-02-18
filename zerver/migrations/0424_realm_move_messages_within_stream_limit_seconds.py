# Generated by Django 4.1.5 on 2023-01-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0423_fix_email_gateway_attachment_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="move_messages_within_stream_limit_seconds",
            field=models.PositiveIntegerField(default=604800, null=True),
        ),
    ]