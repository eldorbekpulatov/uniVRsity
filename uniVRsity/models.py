from django.db import models
from .settings import BASE_DIR

def upload_to(instance, filename):
    return '%s.jpg' % instance.id

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Member(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=25)
    position = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    img = models.ImageField(upload_to = upload_to, blank=True, null=True)
    partOf = models.ManyToManyField(Team)
    email = models.EmailField(max_length = 254)
    facebook = models.URLField(max_length = 254, blank=True)
    twitter = models.URLField(max_length = 254, blank=True)
    gitHub = models.URLField(max_length = 254, blank=True)
    linkedIn = models.URLField(max_length = 254, blank=True)
    instagram= models.URLField(max_length = 254, blank=True)
    googlePlus = models.URLField(max_length = 254, blank=True)



    def __str__(self):
        return self.firstName + ' ' + self.lastName
    def __unicode__(self):
        return self.firstName + ' ' + self.lastName

    class Meta:
        ordering = ('position',)