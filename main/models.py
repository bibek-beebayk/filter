from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def videos_count(self):
        return self.videos.count()


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def videos_count(self):
        return self.videos.count()


class Country(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name

    @property
    def videos_count(self):
        return self.videos.count()


class Video(models.Model):
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='videos')
    genres = models.ManyToManyField(Genre, related_name='videos')
    tags = models.ManyToManyField(Tag, related_name='videos')

    def __str__(self) -> str:
        return self.title