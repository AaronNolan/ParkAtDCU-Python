from django.db import models


# Create your models here.
class Campus(models.Model):
    campus_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Carpark(models.Model):
    carpark_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="campus")
    spaces = models.IntegerField()
    disabled_spaces = models.IntegerField()

    def __str__(self):
        return self.name
