from django.db import models


class Mpaa(models.Model):
    id: models.AutoField(primary_key=True)
    mpaa_type = models.CharField(max_length=10)
    mpaa_label = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "mpaa"


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    genre = models.JSONField(help_text="List of genres")
    language = models.CharField(max_length=50)
    # mpaa_id = models.BigIntegerField(null=True)
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)
    mpaa = models.ForeignKey(
        Mpaa,
        models.DO_NOTHING,
        to_field="id",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "movie"


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "genre"
