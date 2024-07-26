from django.db import models


class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.title} |  {self.author}'
