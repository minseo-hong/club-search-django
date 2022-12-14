from django.db import models


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to="images/")
    sort = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    tag = models.TextField(null=True, blank=True)
    manager = models.CharField(null=True, blank=True, max_length=50)
    manager_call = models.CharField(null=True, blank=True, max_length=50)
    introduction = models.TextField(null=True, blank=True)
    recruit_period = models.CharField(null=True, blank=True, max_length=50)
    recruit_number = models.CharField(null=True, blank=True, max_length=50)
    recruit_way = models.CharField(null=True, blank=True, max_length=50)
    activity_period = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.name
