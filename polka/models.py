from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.author}"

