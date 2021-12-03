from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField

# Create your models here.

class Affiliation(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    content = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    headname = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Referees/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()
    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)


class Referee(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Referees/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()
    
    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)


class Judge(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Judges/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()

    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)

class Examinar(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Judges/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()
    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)

class Author(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Judges/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()
    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)


class BlackBelt(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Judges/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()
    title = models.CharField(max_length=128,blank=True,null=True)
    titletwo = models.CharField(max_length=128,blank=True,null=True)
    titlethree = models.CharField(max_length=128,blank=True,null=True)

    def __str__(self):
        return str(self.name)


class Gallery(models.Model):
    name = models.CharField(max_length=128,blank=True,null=True)
    photo = VersatileImageField('Photo',upload_to="Gallery/",blank=True,null=True,ppoi_field="ppoi")
    ppoi=PPOIField()

    def __str__(self):
        return str(self.name)