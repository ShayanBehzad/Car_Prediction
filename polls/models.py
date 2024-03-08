from django.db import models

class P206_c(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mileage = models.IntegerField()
    model = models.IntegerField()
    trim = models.IntegerField()
    price = models.IntegerField()


class l90_c(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mileage = models.IntegerField()
    model = models.IntegerField()
    trim = models.IntegerField()
    price = models.IntegerField()

class Pride_c(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mileage = models.IntegerField()
    model = models.IntegerField()
    trim = models.IntegerField()
    price = models.IntegerField()
