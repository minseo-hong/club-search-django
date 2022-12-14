# Generated by Django 4.1.4 on 2022-12-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "club_search",
            "0002_club_introduction_alter_club_logo_alter_club_manager_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="activity_period",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="club",
            name="recruit_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="club",
            name="recruit_period",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="club",
            name="recruit_way",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
