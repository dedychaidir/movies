# Generated by Django 5.1.4 on 2024-12-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies_app", "0002_genre_mpaa_remove_movie_mpaa_label_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mpaa",
            name="mpaa_type",
            field=models.CharField(max_length=100),
        ),
    ]
