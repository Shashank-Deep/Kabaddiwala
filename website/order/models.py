from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    page_rate = models.IntegerField()
    glass_rate = models.IntegerField()
    metal_rate = models.IntegerField()
    phone_no = models.CharField(max_length=20)
