from django.db import models


class Basetable(models.Model):
    basetable_id = models.AutoField(primary_key=True)
    photourls = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Tags(models.Model):
    tags_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    basetable_id = models.ForeignKey(Basetable, on_delete=models.CASCADE)
# from django.db import models
#
# # Create your models here.
# class Pet(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     category = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     photoUrls = models.CharField(max_length=255)
#     tags = models.CharField(max_length=255)
#     status = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
