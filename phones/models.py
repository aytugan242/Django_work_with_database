from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.URLField(default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(default=None)

    def __str__(self):
        return f'{self.id}. {self.name}'
