from django.db import models
from django.db.models import CharField


class PredResults(models.Model):
    Age = models.FloatField() 
    Object_Rating = models.IntegerField()
    BodyPart_Rating = models.IntegerField()
    Gender = models.CharField(max_length=30)
    Delivery = models.CharField(max_length=30)
    Birth_Injury = models.CharField(max_length=30)
    Jaundice = models.CharField(max_length=30)
    Cousin_Marriage = CharField(max_length=30)
    Q1 = models.CharField(max_length=30)
    Q2 = models.CharField(max_length=30)
    Q3 = models.CharField(max_length=30)
    Q4 = models.CharField(max_length=30)
    Q5 = models.CharField(max_length=30)
    Q6 = models.CharField(max_length=30)
    Q7 = models.CharField(max_length=30)
    Q8 = models.CharField(max_length=30)
    Q9 = models.CharField(max_length=30)
    Q10 = models.CharField(max_length=30)
    Q11 = models.CharField(max_length=30)
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name
