# Generated by Django 4.1.6 on 2023-02-25 01:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0430_fix_audit_log_objects_for_group_based_stream_settings"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="archivedreaction",
            unique_together={("user_profile", "message", "reaction_type", "emoji_code")},
        ),
        migrations.AlterUniqueTogether(
            name="reaction",
            unique_together={("user_profile", "message", "reaction_type", "emoji_code")},
        ),
    ]