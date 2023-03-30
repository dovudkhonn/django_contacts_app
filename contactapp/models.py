from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    number = models.IntegerField()
    relation = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.relation
