from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    photoUrls = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
