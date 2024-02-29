from django.db import models

# Create your models here.


class jobnew(models.Model):
    position = models.CharField(max_length = 100)
    job_time = models.CharField(max_length = 100)
    job_type = models.CharField(max_length = 100)
    place_of_work = models.CharField(max_length = 100)
    posted_date = models.DateField(auto_now_add = True)
    deadline = models.DateField()