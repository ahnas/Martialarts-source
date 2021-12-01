from django.db import models
from versatileimagefield.fields import VersatileImageField

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=128)
    photo = VersatileImageField('Photo',upload_to="Referees/")
    title = models.CharField(max_length=128)
    titletwo = models.CharField(max_length=128)
    titlethree = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Referee(models.Model):
    name = models.CharField(max_length=128)
    photo = VersatileImageField('Photo',upload_to="Referees/")
    title = models.CharField(max_length=128)
    titletwo = models.CharField(max_length=128)
    titlethree = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Judge(models.Model):
    name = models.CharField(max_length=128)
    photo = VersatileImageField('Photo',upload_to="Judges/")
    title = models.CharField(max_length=128)
    titletwo = models.CharField(max_length=128)
    titlethree = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

class Examinar(models.Model):
    name = models.CharField(max_length=128)
    photo = VersatileImageField('Photo',upload_to="Judges/")
    title = models.CharField(max_length=128)
    titletwo = models.CharField(max_length=128)
    titlethree = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    name = models.CharField(max_length=128)
    photo = VersatileImageField('Photo',upload_to="Judges/")
    title = models.CharField(max_length=128)
    titletwo = models.CharField(max_length=128)
    titlethree = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)