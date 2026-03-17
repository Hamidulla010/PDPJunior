from django.db import models


class Contact(models.Model):
    name = models.CharField()
    course = models.CharField(null=True, blank=True)
    phone_number = models.CharField()

    def __str__(self):
        return self.name



class Mentors(models.Model):
    image = models.ImageField()
    name = models.CharField()
    job = models.CharField()

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    image = models.ImageField()
    auther_image = models.ImageField()
    title = models.CharField()
    auther = models.CharField()

    def __str__(self):
        return self.title

