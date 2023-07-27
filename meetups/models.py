from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Partcipant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=100)
    organizer_email = models.EmailField(null=True)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Partcipant, blank=True, null=True)
